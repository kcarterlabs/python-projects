from ping3 import ping

def ping_host(host):
    response = ping(host, timeout=2)
    if response is None:
        print(f"{host} is unreachable")
    else:
        print(f"Ping to {host}: {response * 1000:.2f} ms")

