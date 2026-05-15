import os


def list_folder_contents(folder_path):

    print(f"\nChecking folder: {folder_path}")

    try:
        items = os.listdir(folder_path)

        if not items:
            print("Folder is empty")
            return

        print("Files and folders found:")

        for item in items:
            print(f"  - {item}")

    except FileNotFoundError:
        print("ERROR: Folder does not exist")

    except PermissionError:
        print("ERROR: Permission denied")

    except Exception as error:
        print(f"Unexpected error: {error}")


def main():

    user_input = input(
        "Enter folder paths separated by spaces: "
    )

    folder_list = user_input.split()

    if not folder_list:
        print("No folders provided")
        return

    for folder in folder_list:
        list_folder_contents(folder)


main()