import base64
import json
from PIL import Image
from io import BytesIO
from stegano import lsb

def decode_base64_to_image(base64_string, output_path, metadata):
    # Decode base64 string
    decoded_data = base64.b64decode(base64_string)

    # Convert decoded data to an image object
    img_data = BytesIO(decoded_data)
    image = Image.open(img_data)

    # Save the image as a bitmap
    image_path = "temp_image.bmp"
    image.save(image_path, format='BMP')

    # Embed metadata into the image using steganography
    secret_image = lsb.hide(image_path, metadata)
    secret_image.save(output_path)

def extract_metadata_to_json(image_path, output_path):
    # Reveal the hidden metadata from the image
    hidden_metadata = lsb.reveal(image_path)

    # Load the metadata into a dictionary
    try:
        metadata_dict = json.loads(hidden_metadata)
    except json.JSONDecodeError:
        print(f"Error: The hidden metadata in {image_path} is not a valid JSON string.")
        return

    # Write the dictionary to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(metadata_dict, json_file, indent=4)

# Metadata to be encrypted in the image
metadata_dict = {
    "Token Designation": "BRC-69",
    "Satoshi Number": "XXXXXXXXXXXXXXXX",
    "Parent Satoshi Number": "XXXXXXXXXXXXXXXX",
    "Collection Name": "Name",
    "Collection Size": "XXXX",
    "Collection Number": "XXXX/XXXX",
    "Background": "<value>",
    "Trait 1": "<value>",
    "Trait 2": "<value>",
    "Trait 3": "<value>",
    "Trait 4": "<value>",
    "Trait 5": "<value>",
    "Trait 6": "<value>",
    "Trait 7": "<value>"
}

# Convert the dictionary to a JSON string
metadata = json.dumps(metadata_dict)
 