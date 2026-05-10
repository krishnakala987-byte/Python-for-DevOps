import sys

disk_usage = int(sys.argv[1])

if disk_usage > 90:
    print("Disk Almost Full")

else:
    print("Disk Usage Normal")