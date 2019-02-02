import grpc
from concurrent import futures
import time

# Import grpc classes
import tsns_pb2
import tsns_pb2_grpc 

# Class for the service
class tsnsServicer(tsns_pb2_grpc.TinySocialNetworkServiceServicer):

	def Follow(self, request, context):
		response = tsns_pb2.ToggleFollow()
		response.Origin = request.Origin
		response.Target = request.Target
		response.Following = True
		return response


	def Unfollow(self, request, context):
		response = tsns_pb2.ToggleFollow()
		response.Origin = request.Origin
		response.Target = request.Target
		response.Following = False
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
