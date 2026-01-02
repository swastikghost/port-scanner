import socket
from datetime import datetime

# Target input
target = input("Enter target IP or website: ")

# Resolve hostname
target_ip = socket.gethostbyname(target)

print("-" * 50)
print("Scanning Target:", target_ip)
print("Scanning started at:", datetime.now())
print("-" * 50)

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nScan stopped by user")

except socket.gaierror:
    print("\nHostname could not be resolved")

except socket.error:
    print("\nServer not responding")

print("\nScanning completed at:", datetime.now())
