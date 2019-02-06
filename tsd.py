import grpc
from concurrent import futures
import time
import os
import json
import copy

# Import grpc classes
import tsns_pb2
import tsns_pb2_grpc 

userTemplate = {
"username": "",
"followers": [],
"following": [],
"posts": [],
"timeline": []
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
			print(self.currentUsers)	

	def saveAll(self):
		users = self.currentUsers.keys()
		for user in users:
			self.save(user)

	def save(self, username):
		with open(os.path.join(os.getcwd(), "users/" + username + ".json"), "w") as saveFile:
			print("Saving..." + json.dumps(self.currentUsers[username]))
			json.dump(self.currentUsers[username], saveFile)
			saveFile.close()

	def Login(self, request, context):
		username = request.Username
		if username not in self.currentUsers:
			print("Making user account.")
			newUser = copy.deepcopy(userTemplate)
			newUser["username"] = username
			self.currentUsers[newUser["username"]] = copy.deepcopy(newUser)
			self.save(username)
		else:
			print(username + " logged in.")
		response = tsns_pb2.Auth()
		response.Username = username
		response.Password = request.Password
		response.LoggedIn = True
		return response

	def Follow(self, request, context):
		response = tsns_pb2.ToggleFollow()
		username = request.Origin
		target = request.Target
		response.Origin = username
		response.Target = target 
		if username not in self.currentUsers.keys():
			response.Following = False
			return response
		following = self.currentUsers[username]["following"]
		followers = self.currentUsers[target]["followers"]
		if target in following:
			response.Following = True
			return response 
		following.append(target)
		self.save(username)
		if username in followers:
			response.Following = True
			return response
		followers.append(username)	
		self.save(target)
		response.Following = True
		return response


	def Unfollow(self, request, context):
		response = tsns_pb2.ToggleFollow()
		username = request.Origin
		target = request.Target
		response.Origin = username
		response.Target = target 
		if username not in self.currentUsers.keys():
			response.Following = True
			return response
		following = self.currentUsers[username]["following"]
		followers = self.currentUsers[target]["followers"]
		if target not in following:
			response.Following = False
			return response 
		following.remove(target)
		self.save(username)
		if username not in followers:
			response.Following = False
			return response
		followers.remove(username)	
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
			currentFollowersList += user + " "
		response.CurrentUsers = currentUsersList
		response.Followers = currentFollowersList
		return response

# Create the server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add class to server
tsns_pb2_grpc.add_TinySocialNetworkServiceServicer_to_server(tsnsServicer(), server)

# Listen on port 8888
print("Starting server on port 8888")
server.add_insecure_port("[::]:8888")
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)
