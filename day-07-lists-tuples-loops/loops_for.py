# For Loops in Python

services = ["EC2", "S3", "Lambda", "IAM"]

print("AWS Services:\n")

for service in services:
    print(service)

print("\nUsing range()\n")

for number in range(1, 6):
    print(number)

print("\nEven Numbers\n")

for even in range(0, 11, 2):
    print(even)