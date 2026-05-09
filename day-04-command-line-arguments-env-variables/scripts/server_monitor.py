import sys

cpu_usage = int(sys.argv[1])

if cpu_usage > 80:
    print("High CPU Usage")
else:
    print("System Healthy")