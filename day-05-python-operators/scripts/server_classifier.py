import sys

server_id = int(sys.argv[1])

if server_id % 2 == 0:
    print("Production Server")

else:
    print("Staging Server")