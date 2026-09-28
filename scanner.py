import socket
from concurrent.futures import ThreadPoolExecutor
target = input("Enter target Ip or domain: ")
def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))
        try:
            s.send(b"Hello\r\n")
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"
        s.close()
        print(f"Port {port} open -> {banner}")
        return f"Port {port} open -> {banner}"
    except:
        return None
results = []
with ThreadPoolExecutor(max_workers=100) as executor:
    for r in executor.map(scan_port, range(1, 1025)):
        if r:
            results.append(r)
with open("result.txt", "w") as f:
    for line in results:
        f.write(line + "\n")
print("Done, saved to result.txt")

