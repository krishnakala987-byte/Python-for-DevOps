import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument(
    "folders",
    nargs="+",
    help="Folder paths"
)

args = parser.parse_args()


for folder in args.folders:

    print(f"\nChecking: {folder}")

    try:

        items = os.listdir(folder)

        if not items:

            print("Folder is empty")

        else:

            for item in items:

                print(item)

    except FileNotFoundError:

        print("Folder does not exist")

    except PermissionError:

        print("Permission denied")

    except Exception as error:

        print(f"Unexpected error: {error}")