try:

    file = open("missing.txt", "r")

except FileNotFoundError:

    print("File does not exist")