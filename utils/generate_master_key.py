# utils/generate_master_key.py

"""
Generates a Fernet encryption key for secure note encryption.
Run this script and copy the output into your .env file like so:

FERNET_KEY=your-generated-key-here
"""

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key().decode()
    print(f"FERNET_KEY={key}")

if __name__ == "__main__":
    generate_key()
