import random
import string
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_cipher(master_pwd):
    """Generates an encryption key from the master password."""
    password = master_pwd.encode()
    salt = b'fixed_salt_for_demo'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                     salt=salt, iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return Fernet(key)


def generate_random_password(length=16):
    """Creates a high-entropy random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


def check_pwd_strength(pwd):
    """Returns a tuple (Strength String, Color) based on complexity."""
    if len(pwd) < 8:
        return "Weak", "red"
    has_digit = any(c.isdigit() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)

    if has_digit and has_upper and has_special and len(pwd) >= 12:
        return "Strong", "green"
    return "Medium", "orange"
