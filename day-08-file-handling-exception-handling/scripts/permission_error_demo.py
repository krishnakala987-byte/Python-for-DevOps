try:

    file = open("/root/secret.txt", "r")

    content = file.read()

    print(content)

except PermissionError:

    print("Permission denied")

except Exception as error:

    print(f"Unexpected error: {error}")