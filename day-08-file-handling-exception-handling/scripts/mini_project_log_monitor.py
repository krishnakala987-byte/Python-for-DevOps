import os


log_folder = input("Enter log folder path: ")


try:

    files = os.listdir(log_folder)

    log_files = []

    for file in files:

        if file.endswith(".log"):

            log_files.append(file)

    if not log_files:

        print("No log files found")

    else:

        print("\nLog files found:\n")

        for log in log_files:

            print(log)

except FileNotFoundError:

    print("Log folder does not exist")

except PermissionError:

    print("Permission denied")

except Exception as error:

    print(f"Unexpected error: {error}")