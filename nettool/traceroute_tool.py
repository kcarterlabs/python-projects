from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

def traceroute(dest, max_hops=30):
    print(f"Traceroute to {dest} (max {max_hops} hops):")
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=dest, ttl=ttl) / ICMP()
        reply = sr1(pkt, verbose=0, timeout=1)
        if reply:
            print(f"{ttl:2d}: {reply.src}")
            if reply.src == dest:
                break
        else:
            print(f"{ttl:2d}: *")

