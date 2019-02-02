import grpc
import sys

# Import grpc classes
import tsns_pb2
import tsns_pb2_grpc

# Creating a grpc channel
channel = grpc.insecure_channel(sys.argv[1] + ":" + sys.argv[2])

# Creating a grpc stub
stub = tsns_pb2_grpc.TinySocialNetworkServiceStub(channel)

# Creating a follow request
follow = tsns_pb2.ToggleFollow(Origin="thomas", Target="shawn", Following=False)

# Making the call
response = stub.Follow(follow)

# Checking
print("Response: " + response.Origin + ", " + response.Target + ", " + reponse.Following)
