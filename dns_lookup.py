import socket

print("=== DNS Lookup Tool ===")

domain = input("Enter domain name: ")

try:
    ip_address = socket.gethostbyname(domain)
    print(f"IP Address: {ip_address}")
except socket.gaierror:
    print("Invalid domain or unable to resolve.")
