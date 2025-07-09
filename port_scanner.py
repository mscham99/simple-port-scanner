import socket
from datetime import datetime

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    print(f"Time started: {datetime.now()}")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP address or hostname: ")
    
    # Common ports you can adjust or expand
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]

    scan_ports(target, ports_to_scan)
