# headers_tool.py

import requests

def show_headers(url):
    try:
        print(f"\nFetching headers for: {url}\n")
        response = requests.head(url, allow_redirects=True, timeout=5)
        print(f"Final URL: {response.url}")
        print(f"Status Code: {response.status_code}\n")
        print("Response Headers:")
        for k, v in response.headers.items():
            print(f"{k}: {v}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")

