import sys

cpu = int(sys.argv[1])

if cpu > 80:
    print("Critical CPU Usage")

else:
    print("System Healthy")