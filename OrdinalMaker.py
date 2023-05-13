import os
import base64
import json
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# This script creates a table of paired hashes that can be inscribed as BRC-69 Ordinals using an input of a JSON folder containing metadata and another JSON folder containing base64 encoded Bitmap images. 
   
def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()
        base64_code = base64.b64encode(image_bytes).decode('utf-8')
        return base64_code

def folder_to_base64_json(folder_path):
    base64_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.bmp'):
            image_path = os.path.join(folder_path, filename)
            base64_code = image_to_base64(image_path)
            base64_data.append({'Filename': filename, 'Base64 Code': base64_code})
    return base64_data

def save_base64_json(base64_data, folder_path):
    json_file_path = os.path.join(folder_path, 'base64_data.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(base64_data, json_file, indent=4)

def encrypt_base64_data(base64_data, aes_key):
    # Derive a key from the provided AES key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=os.urandom(16),
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(aes_key.encode())

    # Create a new AES cipher
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()

    # Padding
    padder = sym_padding.PKCS7(128).padder()

    # Encrypt the base64 strings
    encrypted_data = []
    for entry in base64_data:
        base64_code = entry['Base64 Code']
        encrypted_code = encryptor.update(padder.update(base64_code.encode()) + padder.finalize()) + encryptor.finalize()
        encrypted_data.append({'Filename': entry['Filename'], 'Encrypted Code': encrypted_code.hex()})
    
    return encrypted_data

def main(folder_path, aes_key):
    # Convert images to Base64 and create the JSON data
    base64_data = folder_to_base64_json(folder_path)

    # Encrypt the Base64 data
    encrypted_data = encrypt_base64_data(base64_data, aes_key)

    # Save the encrypted data as JSON in the same folder
    save_base64_json(encrypted_data, folder_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a database of paired hashes')
    parser.add_argument('--folder', metavar='folder', required=True, help='path to the folder containing BMP images')
    parser.add_argument('--key', metavar='key', required=True, help='AES key for encryption')
    args = parser.parse_args()

    # Execute the main function with the provided folder path and AES key
    main(args.folder, args.key)
