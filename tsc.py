import grpc
import sys
import subprocess

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

def proccess_command(c, u):
    if c == "LIST":
	listuser = tsns_pb2.ListUser(Origin=u)
	reply = stub.List(listuser)
        print("Users: " + reply.CurrentUsers + "Followers: " + reply.Followers)
    elif c == "TIMELINE":
	print("Now you are in the timeline")
        try:
		while True:
			text = raw_input()
			post = tsns_pb2.Post(Origin=u, Post=text, Time="0")
			stub.MakePost(post)
			timelinereq = tsns_pb2.TimelineRequest(Origin=u)
			for receivedPost in stub.Timeline(timelinereq):
				print(receivedPost.Origin + " " + receivedPost.Time + " " + receivedPost.Post)
	except KeyboardInterrupt():
		pass
    else:
	command, user = c.split(" ", 1)
    	if command == "FOLLOW":
        	follow = tsns_pb2.ToggleFollow(Origin=u, Target=user, Following=False)
        	r = stub.Follow(follow)
		print("Response: " + r.Origin + ", " + r.Target + ", " + str(r.Following))
    	elif command == "UNFOLLOW":
		unfollow = tsns_pb2.ToggleFollow(Origin=u, Target=user, Following=False)
		r = stub.Unfollow(unfollow)
		print("Response: " + r.Origin + ", " + r.Target + ", " + str(r.Following))
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
stub.Login(login)

while(True):
	#Displaying title
	display_title()
	#Getting command input by user
	command = get_command()
	r = proccess_command(command, username)
	
	










