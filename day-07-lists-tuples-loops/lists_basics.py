# Lists in Python

servers = ["web-server", "db-server", "cache-server"]

print("Servers List:")
print(servers)

print("\nFirst Server:")
print(servers[0])

print("\nAdding New Server")
servers.append("backup-server")

print(servers)

print("\nRemoving Cache Server")
servers.remove("cache-server")

print(servers)

print("\nTotal Servers:")
print(len(servers))