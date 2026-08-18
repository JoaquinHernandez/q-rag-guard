from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.backends import default_backend

# 1. Quantum Vulnerable RSA Key Generation
def generate_legacy_rsa():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

# 2. Quantum Vulnerable Elliptic Curve Signing Key
def generate_legacy_ecdsa():
    curve = ec.SECP256R1()
    private_key = ec.generate_private_key(curve, default_backend())
    return private_key

if __name__ == "__main__":
    print("Application initialized with cryptographic assets.")
