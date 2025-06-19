import argparse
from dns_tool import dns_lookup
from ping_tool import ping_host
from traceroute_tool import traceroute
from netcat_tool import netcat_connect
from nmap_tool import stealth_scan
from headers_tool import show_headers
from istio_tool import envoy_stats
from istioctl_tool import analyze_istio_config

def main():
    parser = argparse.ArgumentParser(description="Python Network Debug Tool")
    subparsers = parser.add_subparsers(dest="command")

    # DNS Command
    dns_parser = subparsers.add_parser("dns", help="Perform DNS lookup")
    dns_parser.add_argument("domain", help="Domain to resolve")

    # Ping Command
    ping_parser = subparsers.add_parser("ping", help="Ping a host")
    ping_parser.add_argument("host", help="Host to ping")

    # Traceroute Command
    trace_parser = subparsers.add_parser("traceroute", help="Traceroute to host")
    trace_parser.add_argument("host", help="Host to trace")

    # Netcat Command
    nc_parser = subparsers.add_parser("netcat", help="Connect to host:port (like netcat)")
    nc_parser.add_argument("host", help="Target host")
    nc_parser.add_argument("port", type=int, help="Target port")

    # nmap Command
    nmap_parser = subparsers.add_parser("nmap", help="Silently scan target")
    nmap_parser.add_argument("target", help="IP or CIDR range to scan")

    # headers Command
    headers_parser = subparsers.add_parser("headers", help="Show HTTP response headers")
    headers_parser.add_argument("url", help="Target URL (e.g., https://example.com)")

    # istio Command
    istio_parser = subparsers.add_parser(
    "istio", help="Query Istio Envoy admin stats or run istioctl analyze"
    )
    istio_parser.add_argument(
    "--pod-ip", default="127.0.0.1", help="Pod IP with Istio sidecar (default: 127.0.0.1)"
    )
    istio_parser.add_argument(
    "--admin-port", type=int, default=15000, help="Envoy admin port (default: 15000)"
    )
    istio_parser.add_argument(
    "--analyze", action="store_true", help="Run istioctl analyze instead of fetching stats"
    )
    istio_parser.add_argument(
    "--namespace", default="default", help="Namespace for istioctl analyze (default: default)"
    )

    # s_client command
    parser_ssl = subparsers.add_parser("sslcheck", help="Check TLS/SSL on a host")
    parser_ssl.add_argument("host", help="Hostname or IP")
    parser_ssl.add_argument("-p", "--port", type=int, default=443, help="Port (default: 443)")
    parser_ssl.add_argument("--insecure", action="store_true", help="Skip cert validation")
    parser_ssl.add_argument("--export", action="store_true", help="Export leaf certificate to server_cert.pem")

    args = parser.parse_args()
    
    if args.command == "dns":
        dns_lookup(args.domain)
    elif args.command == "ping":
        ping_host(args.host)
    elif args.command == "traceroute":
        traceroute(args.host)
    elif args.command == "netcat":
        netcat_connect(args.host, args.port)
    elif args.command == "nmap":
        stealth_scan(args.target)
    elif args.command == "headers":
        show_headers(args.url)
    elif args.command == "istio":
        if args.analyze:
            analyze_istio_config(namespace=args.namespace)
        else:
            envoy_stats(pod_ip=args.pod_ip, port=args.admin_port)
    elif args.command == "sslcheck":
        from ssl_tool import ssl_check
        ssl_check(args.host, args.port, args.insecure, args.export)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

