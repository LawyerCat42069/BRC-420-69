from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from os import urandom
import base64
import json

def encrypt_base64_pairs():
    # Prompt for the input JSON file
    json_file = input("Enter the path to the input JSON file: ")

    # Prompt for the private key file
    private_key_file = input("Enter the path to the private key file: ")

    # Prompt for the output directory
    output_dir = input("Enter the path to the output directory: ")

    # Read the input JSON file
    with open(json_file, 'r') as f:
        base64_data = json.load(f)

    # Load the private key from file
    with open(private_key_file, 'rb') as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

    # Initialize the encrypted data list
    encrypted_data = []

    # Iterate over the base64 pairs and encrypt them
    for pair in base64_data:
        base64_str1 = pair["Base64 String 1"].encode()
        base64_str2 = pair["Base64 String 2"].encode()

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

        # Store the encrypted data in a dictionary
        encrypted_pair = {
            "Encrypted String 1": base64.b64encode(encrypted_str1).decode(),
            "Encrypted String 2": base64.b64encode(encrypted_str2).decode()
        }

        # Append the encrypted pair to the encrypted data list
        encrypted_data.append(encrypted_pair)

    # Generate the output JSON file path
    output_file = f"{output_dir}/encrypted_data.json"

    # Write the encrypted data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(encrypted_data, f, indent=4)

    print(f"Encrypted data saved to: {output_file}")

if __name__ == "__main__":
    encrypt_base64_pairs()
