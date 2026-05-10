import sys

cpu = int(sys.argv[1])
memory = int(sys.argv[2])

if cpu > 80 and memory > 80:
    print("Critical Infrastructure Alert")

elif cpu > 70 or memory > 70:
    print("Warning Infrastructure Alert")

else:
    print("Infrastructure Healthy")