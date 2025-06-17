import dns.resolver

def dns_lookup(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        for ip in result:
            print(f"A record for {domain}: {ip.to_text()}")
    except Exception as e:
        print(f"DNS lookup failed: {e}")

