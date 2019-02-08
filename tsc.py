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
    text = input('Cmd>')
    return text

def proccess_command(c, u):
    
    if c == "FOLLOW":
        follow = tsns_pb2.ToggleFollow(Origin=u, Target="shawn", Following=False)
        stub.Follow(follow)
    elif c == "UNFOLLOW":
        print("UNFOLLOW")
    elif c == "LIST":
        print("LIST")
    elif c == "TIMELINE":
        print("TIMELINE")
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


#Displaying title
display_title()
#Getting command input by user
command = get_command()
proccess_command(command, username)



# Creating a follow request
follow = tsns_pb2.ToggleFollow(Origin="thomas", Target="shawn", Following=False)

# Making the call
response = stub.Follow(follow)

# Checking
print("Response: " + response.Origin + ", " + response.Target + ", " + str(response.Following))


