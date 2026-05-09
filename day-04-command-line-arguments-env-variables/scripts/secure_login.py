import os

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

print(f"Logging in with user: {username}")
print("Password retrieved securely")