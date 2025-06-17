import socket

def netcat_connect(host, port):
    try:
        with socket.create_connection((host, port), timeout=3) as sock:
            print(f"Connected to {host}:{port}")
            sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            response = sock.recv(4096)
            print(response.decode(errors="ignore"))
    except Exception as e:
        print(f"Connection failed: {e}")

