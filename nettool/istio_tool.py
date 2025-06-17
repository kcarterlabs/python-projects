import requests
import subprocess

def envoy_stats(pod_ip="127.0.0.1", port=15000):
    url = f"http://{pod_ip}:{port}/stats"
    try:
        print(f"Fetching Envoy stats from {url}")
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(response.text[:2000])  # Print partial or full
        else:
            print(f"Non-200 response: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to connect to Envoy admin API: {e}")

def analyze_istio_config():
    try:
        output = subprocess.check_output(["istioctl", "analyze", "-n", "default"], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"istioctl analyze failed:\n{e.output.decode()}")
