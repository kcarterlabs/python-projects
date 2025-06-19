import socket
import ssl
from datetime import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import timezone

def parse_cert(cert_der):
    return x509.load_der_x509_certificate(cert_der, default_backend())

def format_name(name):
    return ", ".join(f"{attr.oid._name}={attr.value}" for attr in name)

def print_cert_info(cert, index=None):
    if index is not None:
        print(f"\nCertificate #{index + 1} in chain:")
    else:
        print("\nCertificate:")

    print(f"  Subject: {format_name(cert.subject)}")
    print(f"  Issuer: {format_name(cert.issuer)}")
    print(f"  Valid from: {cert.not_valid_before_utc}")
    print(f"  Valid until: {cert.not_valid_after_utc}")

    # Check for wildcard in CN or SANs
    cn = None
    try:
        cn = cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
    except IndexError:
        pass

    wildcards = []
    if cn and "*" in cn:
        wildcards.append(cn)

    try:
        sans = cert.extensions.get_extension_for_oid(x509.ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
        for entry in sans.value.get_values_for_type(x509.DNSName):
            if "*" in entry:
                wildcards.append(entry)
    except x509.ExtensionNotFound:
        pass

    if wildcards:
        print(f" Wildcard domains found: {', '.join(wildcards)}")
    else:
        print(" No wildcard domains found.")

    # Expiry check
    days_left = (cert.not_valid_after_utc- datetime.now(timezone.utc)).days
    print(f"  Days until expiry: {days_left}")
    if days_left < 30:
        print("  ⚠️ Warning: Certificate expires soon!")
    if days_left < 0:
        print("Certificate is expired!")

def ssl_check(host, port=443, insecure=False, export=False):
    context = ssl.create_default_context()
    if insecure:
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                print(f"\nConnected to {host}:{port}")
                print(f"TLS Version: {ssock.version()}")
                print(f"Cipher: {ssock.cipher()}")

                # The full chain DERs
                der = ssock.getpeercert(binary_form=True)
                der_chain = [der] if der else []
                if not der_chain:
                    # fallback if get_peer_cert_chain() not available
                    der_chain = [ssock.getpeercert(binary_form=True)]

                for i, der in enumerate(der_chain):
                    cert = parse_cert(der)
                    print_cert_info(cert, i)
                    if export and i == 0:
                        with open("server_cert.pem", "wb") as f:
                            f.write(cert.public_bytes(ssl.PEM))
                        print("Exported leaf certificate to server_cert.pem")

    except ssl.SSLCertVerificationError as e:
        print(f"Certificate verification failed: {e}")
    except Exception as e:
        print(f"Connection failed: {e}")

