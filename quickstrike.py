#!/usr/bin/env python3

import socket
import sys
import threading
from datetime import datetime

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

open_ports = []
lock = threading.Lock()

# Banner
def banner():
    print(f"""{CYAN}
 ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗
██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝
██║   ██║██║   ██║██║██║     █████╔╝ 
██║▄▄ ██║██║   ██║██║██║     ██╔═██╗ 
╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝
      QuickStrike v2 – Recon Engine
            CTK Academy
{RESET}""")

# Resolve target
def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"{GREEN}[+] Target IP:{RESET} {ip}")
        return ip
    except:
        print(f"{RED}[-] Unable to resolve target{RESET}")
        sys.exit()

# Port scan worker
def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            banner_data = grab_banner(ip, port)
            with lock:
                open_ports.append((port, service, banner_data))
                print(f"{GREEN}[OPEN]{RESET} {port}/{service}")
        s.close()
    except:
        pass

# Banner grabbing
def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner[:80]
    except:
        return "No banner"

# Threaded scan
def threaded_scan(ip, ports):
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Save results
def save_results(target):
    filename = f"quickstrike_{target}_{datetime.now().strftime('%H%M%S')}.txt"
    with open(filename, "w") as f:
        for p in open_ports:
            f.write(f"Port: {p[0]} | Service: {p[1]}\nBanner: {p[2]}\n\n")
    print(f"\n{CYAN}[+] Results saved to:{RESET} {filename}")

# Main
def main():
    banner()

    if len(sys.argv) != 4:
        print(f"{YELLOW}Usage:{RESET} python3 quickstrike_v2.py <target> <start_port> <end_port>")
        sys.exit()

    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    ip = resolve_target(target)
    ports = range(start_port, end_port + 1)

    print(f"{CYAN}[*] Scanning ports {start_port}-{end_port}...{RESET}\n")
    threaded_scan(ip, ports)
    save_results(target)

if __name__ == "__main__":
    main()
