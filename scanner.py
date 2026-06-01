import socket
from concurrent.futures import ThreadPoolExecutor

TARGET = input("Enter target IP or domain: ")

COMMON_PORTS = [
20, 21, 22, 23, 25,
53, 80, 110, 135, 139,
143, 443, 445, 993, 995,
1723, 3306, 3389, 5900, 8080
]

open_ports = []

def scan_port(port):
try:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

```
    result = sock.connect_ex((TARGET, port))

    if result == 0:
        open_ports.append(port)
        print(f"[OPEN] Port {port}")

    sock.close()

except Exception:
    pass
```

print(f"\nScanning {TARGET}...\n")

with ThreadPoolExecutor(max_workers=100) as executor:
executor.map(scan_port, COMMON_PORTS)

print("\nScan Complete")

if open_ports:
print("\nOpen Ports:")
for port in sorted(open_ports):
print(f"- {port}")
else:
print("No open ports found.")
