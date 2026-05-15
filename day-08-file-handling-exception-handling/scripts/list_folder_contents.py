import os


folder = input("Enter folder path: ")


try:

    items = os.listdir(folder)

    print("\nFiles and folders found:\n")

    for item in items:

        print(item)

except FileNotFoundError:

    print("Folder does not exist")

except PermissionError:

    print("Permission denied")

except Exception as error:

    print(f"Unexpected error: {error}")