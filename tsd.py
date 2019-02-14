#!/usr/bin/python

import grpc
from concurrent import futures
import time
import os
import json
import copy
import sys

# Import grpc classes
import tsns_pb2
import tsns_pb2_grpc 

userTemplate = {
"username": "",
"followers": [],
"following": [],
"posts": [],
"timeline": [],
"timelineUpdates": []
}

# Class for the service
class tsnsServicer(tsns_pb2_grpc.TinySocialNetworkServiceServicer):
	
	def __init__(self):
		# First load all of the current users information
		self.currentUsers = {}
		# Creating directory for storing user information if it does not already exist
		if not os.path.isdir("./users"):
			os.mkdir("./users/")
		else:
			dirs = os.listdir("./users/")
			files = []
			for f in dirs:
				files.append(f)
			for f in files:
				nextUser = {}
				with open(os.path.join(os.getcwd(), "users/" + f)) as jsonFile:
					nextUser = json.load(jsonFile)
					self.currentUsers[nextUser["username"]] = copy.deepcopy(nextUser)
					self.currentUsers[nextUser["username"]]["loggedin"] = False

	def saveAll(self):
		users = self.currentUsers.keys()
		for user in users:
			self.save(user)

	def save(self, username):
		with open(os.path.join(os.getcwd(), "users/" + username + ".json"), "w") as saveFile:
			json.dump(self.currentUsers[username], saveFile)
			saveFile.close()

	def Login(self, request, context):
		username = request.Username
		response = tsns_pb2.Auth()
		response.Username = username
		response.Password = request.Password
		if request.LoggedIn == False:
			if username in self.currentUsers:
				if self.currentUsers[username]["loggedin"]:
					response.LoggedIn = False
					return response
				else:
					self.currentUsers[username]["loggedin"] = True
			if username not in self.currentUsers:
				newUser = copy.deepcopy(userTemplate)
				newUser["username"] = username
				self.currentUsers[newUser["username"]] = copy.deepcopy(newUser)
				self.currentUsers[newUser["username"]]["loggedin"] = False
				self.save(username)
			response.LoggedIn = True
			return response
		else:
			self.currentUsers[username]["loggedin"] = False
			response.LoggedIn = False
			return response

	def Follow(self, request, context):
		response = tsns_pb2.ToggleFollow()
		username = request.Origin
		target = request.Target
		response.Origin = username
		response.Target = target 
		if username == target:
			response.Following = False
			return response
		if target not in self.currentUsers.keys():
			response.Following = False
			return response
		followTime = time.time()
		following = self.currentUsers[username]["following"]
		followers = self.currentUsers[target]["followers"]
		# Check first if the target is already following the origin
		for follower in following:
			if follower[0] == target:
				response.Following = False
				return response 
		following.append((target, followTime))
		self.save(username)
		#Check first if the origin is already following the target
		for follower in followers:
			if follower[0] == username:
				response.Following = False
				return response
		followers.append((username, followTime))	
		self.save(target)
		response.Following = True
		return response


	def Unfollow(self, request, context):
		response = tsns_pb2.ToggleFollow()
		username = request.Origin
		target = request.Target
		response.Origin = username
		response.Target = target 
		if target not in self.currentUsers.keys():
			response.Following = True
			return response
		following = self.currentUsers[username]["following"]
		followers = self.currentUsers[target]["followers"]
		# Check if the target is even following
		found = False
		for follower in following:
			if follower[0] == target:
				found = follower
		if not found:
			response.Following = True
			return response 
		following.remove(found)
		self.save(username)
		# Check if the origin is even following the target
		for follower in followers:
			if follower[0] == username:
				found = follower
		if not found:
			response.Following = True
			return response
		followers.remove(found)	
		self.save(target)
		response.Following = False
		return response

	def List(self, request, context):
		response = tsns_pb2.ReturnList()
		username = request.Origin
		currentUsersList = ""
		currentFollowersList = ""
		for user in self.currentUsers.keys():
			currentUsersList += user + " "
		for user in self.currentUsers[username]["followers"]:
			currentFollowersList += user[0] + " "
		response.CurrentUsers = currentUsersList
		response.Followers = currentFollowersList
		return response

	def getFollowTime(self, origin, target):
		if origin == target:
			return 0.0
		following = self.currentUsers[origin]["following"]
		for followee in following:
			# Find the right person and return the timestamp they started following them for
			if followee[0] == target:
				return followee[1]

	def Timeline(self, request, context):
		origin = request.Origin
		timeline = copy.deepcopy(self.currentUsers[origin]["timeline"])
		post = tsns_pb2.Post()
		if len(timeline) > 20:
			timeline = timeline[len(timeline)-20]
		timeline.reverse()
		for timelinePost in timeline:
			if timelinePost[1] >= self.getFollowTime(origin, timelinePost[0]):
				post.Origin = timelinePost[0]
				post.Time = time.asctime(time.localtime(timelinePost[1]))
				post.Post = timelinePost[2]
				yield post

	def MakePost(self, request, context):
		newPost = tsns_pb2.Post()
		newPost.Origin = request.Origin
		newPost.Post = request.Post
		postTime = time.time()
		newPost.Time = time.asctime(time.localtime(postTime))
		print(newPost.Origin + " " + newPost.Time + " " + newPost.Post)
		currentUser = self.currentUsers[newPost.Origin]
		currentUser["posts"].append((copy.deepcopy(newPost.Origin), copy.deepcopy(postTime), copy.deepcopy(newPost.Post)))
		currentUser["timeline"].append((copy.deepcopy(newPost.Origin), copy.deepcopy(postTime), copy.deepcopy(newPost.Post)))
		for follower in currentUser["followers"]:
			self.currentUsers[follower[0]]["timeline"].append((copy.deepcopy(newPost.Origin), copy.deepcopy(postTime), copy.deepcopy(newPost.Post)))
			self.currentUsers[follower[0]]["timelineUpdates"].append((copy.deepcopy(newPost.Origin), copy.deepcopy(postTime), copy.deepcopy(newPost.Post)))
		self.saveAll()
		return newPost	

	def TimelineUpdate(self, request, context):
		newPosts = tsns_pb2.NewPosts()
		username = request.Origin
		newPosts.Origin = username
		updates = self.currentUsers[username]["timelineUpdates"]
		if not updates:
			newPosts.Origin = ""
			newPosts.Post = ""
			newPosts.Time = ""
			newPosts.IsNewPost = False
			yield newPosts
		else:
			for i in range(len(updates)):
				newPosts.Origin = updates[0][0]
				newPosts.Time = time.asctime(time.localtime(updates[0][1]))
				newPosts.Post = updates[0][2]
				newPosts.IsNewPost = True
				updates.pop(0)
				yield newPosts
		self.saveAll()

# Create the server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add class to server
tsns_pb2_grpc.add_TinySocialNetworkServiceServicer_to_server(tsnsServicer(), server)

# Listen on port 8888
print("Starting server on port 8888")
server.add_insecure_port("[::]:" + sys.argv[1])
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)
