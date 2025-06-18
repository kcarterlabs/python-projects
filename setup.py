from setuptools import setup, find_packages

setup(
    name="nettool",
    version="0.1.0",
    description="A versatile network debugging CLI tool with DNS, traceroute, netcat, headers, nmap, and Istio debugging",
    author="Kenneth Carter",
    author_email="kenneth.carter@fake-domain.io",
    url="https://github.com/kcarterlabs/python-projects/nettool",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "python-nmap>=0.7.1",
        "scapy>=2.5.0",
        "dnspython>=2.3.0"
    ],
    entry_points={
        "console_scripts": [
            "nettool=cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: System :: Networking",
    ],
    python_requires='>=3.7',
)

