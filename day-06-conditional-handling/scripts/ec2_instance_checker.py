import sys

instance_type = sys.argv[1]

if instance_type == "t2.micro":
    print("Low Cost Instance")

elif instance_type == "t2.medium":
    print("Medium Cost Instance")

elif instance_type == "t2.xlarge":
    print("High Performance Instance")

else:
    print("Unknown Instance Type")