#!/usr/bin/env python3

import socket
import sys
import time

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
def banner():
    print(f"""{RED}
 ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗
██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝
██║   ██║██║   ██║██║██║     █████╔╝ 
██║▄▄ ██║██║   ██║██║██║     ██╔═██╗ 
╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝

          
        QuickStrike Recon Tool
        Author: CTK Academy
{RESET}""")

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"{YELLOW}[+] Target IP:{RESET} {ip}")
        return ip
    except socket.gaierror:
        print(f"{RED}[-] Could not resolve target{RESET}")
        sys.exit()

# Check alive
def is_alive(ip):
    try:
        socket.create_connection((ip, 80), timeout=2)
        print(f"{GREEN}[+] Host is alive{RESET}")
    except:
        print(f"{YELLOW}[!] Host may be blocking port 80 (continuing scan){RESET}")

# Port scan
def scan_ports(ip):
    print(f"\n{CYAN}[*] Scanning common ports...{RESET}\n")
    ports = [21,22,23,25,53,80,110,139,143,443,445,3306,8080]
    
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            print(f"{GREEN}[OPEN]{RESET} Port {port} ({service})")
        s.close()

# Main
def main():
    banner()
    
    if len(sys.argv) != 2:
        print(f"{YELLOW}Usage:{RESET} python3 quickstrike.py <target>")
        sys.exit()

    target = sys.argv[1]
    ip = resolve_target(target)
    is_alive(ip)
    scan_ports(ip)

if __name__ == "__main__":
    main()
