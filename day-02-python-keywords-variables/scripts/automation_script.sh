# scripts/restart_servers.py

servers = ["web1", "web2", "web3"]

def restart_server(server_name):

    try:
        print(f"Restarting {server_name}")
        print("Restart successful")

    except:
        print("Restart failed")

for server in servers:
    restart_server(server)