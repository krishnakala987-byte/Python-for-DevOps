import sys

cpu = int(sys.argv[1])

if cpu > 80:
    print("Scaling Up Infrastructure")

elif cpu < 30:
    print("Scaling Down Infrastructure")

else:
    print("Infrastructure Stable")