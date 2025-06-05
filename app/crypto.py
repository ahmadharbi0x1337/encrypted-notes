"""
Handle symmetric encryption and decryption of note content.
Relies on a single Frenet key loaded from environment variables.
"""

from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve master encryption key from environment
FERNET_KEY = os.getenv("FERNET_KEY")

if not FERNET_KEY:
    raise ValueError("Missing FERNET_KEY in environment. Did you set it in .env?")

fernet = Fernet(FERNET_KEY)



def encrypt_note_content(content: str) -> str:
    """
    Encrypt plain text note content using Fernet symmetric encryption.

    Args: 
        content (str): The plain text content to encrypt.

    Returns:
        str: Encrypted content as a UTF-8 encoded string.
    """
    return fernet.encrypt(content.encode()).decode()

def decrypt_note_content(ciphertext: str) -> str:
    """
    Decrypt encrypted note content using Fernet.
    
    Args:
        ciphertext (str): Encrypted content string to decrypt.

    Returns:
        str: Decrypted plain text string.
    """
    return fernet.decrypt(ciphertext.encode()).decode()