import os


for root, dirs, files in os.walk("."):

    print(f"\nCurrent Folder: {root}")

    for file in files:

        print(file)