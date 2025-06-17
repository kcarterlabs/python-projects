import subprocess

def analyze_istio_config(namespace="default"):
    """
    Run `istioctl analyze` for the given namespace and print output.
    """
    try:
        print(f"Running 'istioctl analyze -n {namespace}' ...\n")
        output = subprocess.check_output(
            ["istioctl", "analyze", "-n", namespace],
            stderr=subprocess.STDOUT,
            text=True,
        )
        print(output)
    except FileNotFoundError:
        print("Error: istioctl command not found. Please install Istio CLI.")
    except subprocess.CalledProcessError as e:
        print(f"istioctl analyze failed with exit code {e.returncode}:\n{e.output}")

