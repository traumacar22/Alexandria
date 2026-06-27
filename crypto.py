import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

def generate_salt(path="safe/salt.bin"):
    salt = os.urandom(16)
    with open(path, "wb") as f:
        f.write(salt)
    return salt

def load_salt(path="safe/salt.bin"):
    with open(path, "rb") as f:
        return f.read()
    

def derive_key(password: str, salt: bytes):
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length = 32, salt = salt, iterations = 480_000)
    key1 = key.derive(password.encode())
    final_key = base64.urlsafe_b64encode(key1)
    return final_key

def get_fernet(password: str, salt: bytes) -> Fernet:
    key = derive_key(password, salt)
    f = Fernet(key) 
    return f