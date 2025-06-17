import nmap

def stealth_scan(target):
    scanner = nmap.PortScanner()
    print(f"Scanning {target} silently...")

    try:
        # -sS: TCP SYN scan (stealth), -T4: faster, -Pn: skip ping
        scanner.scan(hosts=target, arguments='-sS -T4 -Pn')

        for host in scanner.all_hosts():
            print(f"\nHost: {host} ({scanner[host].hostname()})")
            print(f"State: {scanner[host].state()}")

            for proto in scanner[host].all_protocols():
                print(f"Protocol: {proto}")
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    state = scanner[host][proto][port]['state']
                    print(f"  Port: {port}\tState: {state}")
    except Exception as e:
        print(f"Scan failed: {e}")

