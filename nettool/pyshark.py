from scapy.all import sniff
from scapy.all import sniff, wrpcap

def packet_callback(pkt):
    print(pkt.summary())
    sniff(filter="tcp", count=1000, prn=packet_callback)


def packet_capture(count):
    packets = sniff(count=count)
    wrpcap("capture.pcap", packets)
    print("capture.pcap saved!")
    
if __name__ == "__main__":
    count = int(input("How many packets do you want to sniff?: "))
    packet_capture(count)
