import base64
import json
import bson
from PIL import Image
from io import BytesIO
from stegano import lsb
import packet


salt = "Salt6969420741!"

def read_hash_values(file_path):
    hash_values = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('Hash Value'):
                parts = line.split(':')
                key = parts[0].strip()
                value = parts[1].strip()
                hash_values[key] = value
    return hash_values


def reverse_hashing(hash_value, salt):
    return base64.b64decode(hash_value[len(salt):]).decode('utf-8')


def decode_base64_to_image(base64_string, output_path):
    # Decode base64 string
    decoded_data = base64.b64decode(base64_string)

    # Convert decoded data to an image object
    img_data = BytesIO(decoded_data)
    image = Image.open(img_data)

    # Save the image as a bitmap
    image_path = "temp_image.bmp"
    image.save(image_path, format='BMP')

    return image_path


def decode_and_embed_metadata(image_path, metadata_base64, output_image_path, output_json_path):
    # Decode the hidden metadata from base64
    decoded_metadata = base64.b64decode(metadata_base64)

    # Convert the decoded metadata from BSON to JSON
    try:
        metadata_dict = bson.loads(decoded_metadata)
    except bson.InvalidBSON:
        print(f"Error: The hidden metadata in {image_path} is not a valid BSON string.")
        return

    # Write the metadata to a JSON file
    with open(output_json_path, 'w') as json_file:
        json.dump(metadata_dict, json_file, indent=4)

    # Embed metadata into the image using steganography
    secret_image = lsb.hide(image_path, str(metadata_dict))
    secret_image.save(output_image_path)


if __name__ == "__main__":
    # Read the hash values from the designated text file
    hash_file_path = 'path/to/your/hash_file.txt'
    hash_values = read_hash_values(hash_file_path)

    # Reverse the hashing process to retrieve the base64 strings
    BRC_69 = reverse_hashing(hash_values['Hash Value 1'], salt)
    BRC_69_MD = reverse_hashing(hash_values['Hash Value 2'], salt)

    image_path = decode_base64_to_image(BRC_69, 'path/to/your/directory/decoded_image.bmp')
    decode_and_embed_metadata(
        image_path,
        BRC_69_MD,
        'path/to/your/directory/final_image.bmp',
        'path/to/your/directory/metadata.json'
    )
