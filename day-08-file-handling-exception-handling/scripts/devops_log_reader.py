try:

    with open("/var/log/syslog", "r") as file:

        logs = file.read()

        print(logs)

except FileNotFoundError:

    print("Log file not found")

except PermissionError:

    print("Permission denied")

except Exception as error:

    print(f"Unexpected error: {error}")