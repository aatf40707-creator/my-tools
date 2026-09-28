import socket
from concurrent.futures import ThreadPoolExecutor
target = input("IP: ")
open_ports = []
def scan(p):
    try:
        s = socket.socket()
        s.settimeout(0.8)
        s.connect((target, p))
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"
        print(f"[+] {p} OPEN | {banner}")
        open_ports.append(f"{p} | {banner}")
        s.close()
    except:
        pass
with ThreadPoolExecutor(max_workers=100) as ex:
    ex.map(scan, range(1, 1025))
with open("level4_result.txt", "w") as f:
    for r in open_ports:
        f.write(r + "\n")
print(f"\nDone - {len(open_ports)} open")