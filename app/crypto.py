from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """ Generate a new Fernet Key """
    return Fernet.generate_key()

def save_key(key: bytes):
    """ Save The Key To A File """
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    """ Load The Key From File, or generate it if it doesn't exist """
    if not os.path.exists(KEY_FILE):
        key = generate_key()
        save_key(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    
    return key



# Initialize Fernet Once 

fernet = Fernet(load_key())

def encrypt_note_content(plaintext: str) -> str:
    return fernet.encrypt(plaintext.encode()).decode()

def decrypt_note_content(ciphertext: str) -> str:
    return fernet.decrypt(ciphertext.encode()).decode()