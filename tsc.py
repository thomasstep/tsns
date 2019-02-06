import grpc
import sys

# Import grpc classes
import tsns_pb2
import tsns_pb2_grpc

# Creating a grpc channel
channel = grpc.insecure_channel(sys.argv[1] + ":" + sys.argv[2])

# Creating a grpc stub
stub = tsns_pb2_grpc.TinySocialNetworkServiceStub(channel)

# Logging in
login = tsns_pb2.Auth(Username="thomas", Password="me", LoggedIn=False)
stub.Login(login)

# Logging in
login = tsns_pb2.Auth(Username="shawn", Password="me", LoggedIn=False)
stub.Login(login)

# Logging in
login = tsns_pb2.Auth(Username="stoleru", Password="me", LoggedIn=False)
stub.Login(login)

# Logging in
login = tsns_pb2.Auth(Username="welch", Password="me", LoggedIn=False)
stub.Login(login)

# Creating a follow request
follow = tsns_pb2.ToggleFollow(Origin="thomas", Target="shawn", Following=False)

# Making the call
stub.Follow(follow)

# Creating a follow request
follow = tsns_pb2.ToggleFollow(Origin="shawn", Target="welch", Following=False)

# Making the call
stub.Follow(follow)

# Creating a follow request
follow = tsns_pb2.ToggleFollow(Origin="stoleru", Target="welch", Following=False)

# Making the call
stub.Follow(follow)

listuser = tsns_pb2.ListUser(Origin="welch")
reply = stub.List(listuser)

# Checking
print("Users: " + reply.CurrentUsers + " Followers: " + reply.Followers)

# Creating a follow request
unfollow = tsns_pb2.ToggleFollow(Origin="stoleru", Target="welch", Following=False)

# Making the call
stub.Unfollow(unfollow)

listuser = tsns_pb2.ListUser(Origin="welch")
reply = stub.List(listuser)

# Checking
print("Users: " + reply.CurrentUsers + " Followers: " + reply.Followers)
