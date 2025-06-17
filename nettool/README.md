# NetTool — Network Debugging CLI Tool

A versatile Python-based command-line network debugging tool with modules for DNS lookup, traceroute, netcat-style connection, HTTP header inspection, Nmap silent scans, and Istio service mesh debugging.

---

## Features

- **DNS Lookup:** Perform DNS queries.
- **Traceroute:** Trace the route packets take to a host.
- **Netcat:** Connect to TCP/UDP ports for quick testing.
- **Headers:** Fetch HTTP response headers.
- **Nmap:** Run stealth network scans on IP ranges.
- **Istio:** Query Istio Envoy sidecar stats or run Istio configuration analysis.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/kcarterlabs/python-projects/nettool.git
   cd nettool

   pip install requests python-nmap scapy dnspython


| Command      | Description                 | Arguments/Flags                                |
| ------------ | --------------------------- | ---------------------------------------------- |
| `dns`        | Perform a DNS lookup        | `host` (domain to query)                       |
| `traceroute` | Trace network route to host | `host`                                         |
| `netcat`     | Connect to TCP/UDP port     | `host` `port`                                  |
| `headers`    | Fetch HTTP response headers | `url`                                          |
| `nmap`       | Run stealth Nmap scan       | `target` (IP or CIDR range)                    |
| `istio`      | Istio debugging tool        | Flags:                                         |
|              |                             | `--pod-ip` (default `127.0.0.1`)               |
|              |                             | `--admin-port` (default `15000`)               |
|              |                             | `--analyze` (run `istioctl analyze`)           |
|              |                             | `--namespace` (default `default`, for analyze) |


python cli.py dns example.com

python cli.py traceroute google.com

python cli.py netcat example.com 80

python cli.py headers https://example.com

python cli.py nmap 192.168.1.0/24

python cli.py istio

python cli.py istio --analyze --namespace prod

### Notes: 
Some commands (like traceroute or raw socket operations) may require root privileges.

Make sure istioctl is installed and accessible from your command line to use Istio analyze features.

For Nmap scans, nmap must be installed on your system.

Network access and permissions may limit some commands (e.g., firewall rules, Kubernetes RBAC).

```shell
pip install -r requirements.txt
```
