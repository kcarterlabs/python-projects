from scapy.all import rdpcap
import argparse

def view_pcap(file_path, verbose=False):
    try:
        packets = rdpcap(file_path)
        print(f"\nLoaded {len(packets)} packets from {file_path}\n")

        for i, pkt in enumerate(packets, 1):
            print(f"{i:03d}: {pkt.summary()}")
            if verbose:
                pkt.show()
                print("="*60)
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
    except Exception as e:
        print(f"[!] Error reading pcap: {e}")

def main():
    parser = argparse.ArgumentParser(description="Minimal PCAP Viewer")
    parser.add_argument("file", help="Path to .pcap file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show full packet details")
    args = parser.parse_args()

    view_pcap(args.file, args.verbose)

if __name__ == "__main__":
    main()

