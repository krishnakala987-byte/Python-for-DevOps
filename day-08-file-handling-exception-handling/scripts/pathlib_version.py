from pathlib import Path


path = Path("/var/log")

if path.exists():

    print("Path exists")

else:

    print("Path does not exist")