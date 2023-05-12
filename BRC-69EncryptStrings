from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization, hashes, padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from os import urandom
import base64

# Your base64 strings
base64_str1 = b"Base64 String 1"
base64_str2 = b"Base64 String 2"

# Salt and password for AES
password = b"password"  # This should be a secure, random password in a real use case
salt = urandom(16)

# Derive a key from the password
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = kdf.derive(password)

# Create a new AES cipher
cipher = Cipher(algorithms.AES(key), modes.ECB())
encryptor = cipher.encryptor()

# Padding
padder1 = sym_padding.PKCS7(128).padder()
padder2 = sym_padding.PKCS7(128).padder()

# Pad and encrypt the base64 strings
encrypted_str1 = encryptor.update(padder1.update(base64_str1) + padder1.finalize()) + encryptor.finalize()
encrypted_str2 = encryptor.update(padder2.update(base64_str2) + padder2.finalize()) + encryptor.finalize()

# Write the encrypted strings to a file
with open('encrypted_strings.txt', 'wb') as f:
    f.write(encrypted_str1)
    f.write(b'\n')
    f.write(encrypted_str2)

# Write the password and key to a separate file (NOT recommended in a truly private use case - these keys are intended to be public once parent JSON is inscribed)
with open('password_and_key.txt', 'w') as f:
    f.write('Password: ' + password.decode() + '\n')
    f.write('Key: ' + base64.b64encode(key).decode())
