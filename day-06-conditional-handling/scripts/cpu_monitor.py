import sys

cpu = int(sys.argv[1])

if cpu > 90:
    print("Critical Infrastructure Alert")

elif cpu > 70:
    print("High CPU Usage")

else:
    print("Infrastructure Healthy")