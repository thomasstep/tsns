import grpc
import sys
import subprocess
import thread
import threading
import time

# Import grpc classes
import tsns_pb2
import tsns_pb2_grpc

def display_title():
    print("\n========= TINY SNS CLIENT =========");
    print(" Command Lists and Format:");
    print(" FOLLOW <username>");
    print(" UNFOLLOW <username>");
    print(" LIST ");
    print(" TIMELINE");
    print("=====================================");

def get_command():
    text = raw_input('Cmd>')
    return text

def sending(username):
	while True:
		text = raw_input()
		post = tsns_pb2.Post(Origin=username, Post=text, Time="0")
		stub.MakePost(post)


def receiving(username):
	timelinereq = tsns_pb2.TimelineRequest(Origin=username)
	posts = stub.Timeline(timelinereq)
	for receivedPost in posts:
			print(receivedPost.Origin + " " + receivedPost.Time + " " + receivedPost.Post)
	while True:
		post = tsns_pb2.NewPosts(Origin=username, IsNewPost=False, Post="", Time="0")	
		for receivedPost in stub.TimelineUpdate(post):
			if receivedPost.IsNewPost:
				print(receivedPost.Origin + " " + receivedPost.Time + " " + receivedPost.Post)
		time.sleep(1)
		
		
def proccess_command(c, u):
    if c == "LIST":
	listuser = tsns_pb2.ListUser(Origin=u)
	reply = stub.List(listuser)
        print("Users: " + reply.CurrentUsers + "Followers: " + reply.Followers)
    elif c == "TIMELINE":
	print("Now you are in the timeline")
	thread_sent = threading.Thread(target=sending, args=(u,))
	thread_receiving = threading.Thread(target=receiving, args=(u,))
	
	thread_sent.daemon = True
	thread_receiving.daemon = True

	thread_receiving.start()
	thread_sent.start()	
	while True:
		time.sleep(1)	
    else:
	try: 
		command, user = c.split(" ", 1)
	except ValueError:
		print("Invalid Command")
		return
    	if command == "FOLLOW":
        	follow = tsns_pb2.ToggleFollow(Origin=u, Target=user, Following=False)
        	r = stub.Follow(follow)
		listuser = tsns_pb2.ListUser(Origin=u)
		reply = stub.List(listuser)
		if r.Following == False and r.Origin == r.Target:
			print("Input username already exists, command failed")
		elif r.Following == False and user in reply.CurrentUsers:
			print("Command Failed because you cannot follow someone twice")
		elif r.Following == False:
			print("Command Failed with invalid username")
		else:	
			print("Command completed successfully." + r.Origin + " is now following " + r.Target + ".")
    	elif command == "UNFOLLOW":
		unfollow = tsns_pb2.ToggleFollow(Origin=u, Target=user, Following=False)
		r = stub.Unfollow(unfollow)
		if r.Following == True:
			print("Command failed with invalid username")
		else:
			print("Command completed successfully." + r.Origin + " has unfollowed " + r.Target + ". ")
   	else:
        	print("INVALID COMMAND")

# Creating a grpc channel
channel = grpc.insecure_channel(sys.argv[1] + ":" + sys.argv[2])
# Getting username
username = sys.argv[3]
# Creating a grpc stub
stub = tsns_pb2_grpc.TinySocialNetworkServiceStub(channel)
# Logging in
login = tsns_pb2.Auth(Username=username, Password="me", LoggedIn=False)
response = stub.Login(login)
if response.LoggedIn == False:
	print("Can't login because someone else logged in with same username")
else:
	#keyboard interrupt and the logout 
	#just like TIMELINE
	try:
		while(True):
			#Displaying title
			display_title()
			#Getting command input by user
			command = get_command()
			r = proccess_command(command, username)
	except KeyboardInterrupt:
		logout = tsns_pb2.Auth(Username=username, Password="me", LoggedIn=True)
		response = stub.Login(logout)	
		print("you logged out")
	
	
