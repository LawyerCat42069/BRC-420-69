import base64
import json
import bson
from PIL import Image
from io import BytesIO
from stegano import lsb

def decode_base64_to_image(base64_string, output_path, metadata):
    # Decode base64 string
    decoded_data = base64.b64decode(base64_imagehash)

    # Convert decoded data to an image object
    img_data = BytesIO(decoded_data)
    image = Image.open(img_data)

    # Save the image as a bitmap
    image_path = "temp_image.bmp"
    image.save(image_path, format='BMP')

    # Embed metadata into the image using steganography
    secret_image = lsb.hide(image_path, base64_metadata_hash)
    secret_image.save(output_path)

def extract_metadata_to_json(image_path, output_path):
    # Reveal the hidden metadata from the image
    hidden_metadata = lsb.reveal(image_path)

    # Decode the hidden metadata from base64
    decoded_metadata = base64.b64decode(base64_metadata_hash).decode('utf-8')
  
    # Convert the decoded metadata from BSON to JSON

    try:
        metadata_dict = bson.loads(decoded_metadata)
    except bson.InvalidBSON:
        print(f"Error: The hidden metadata in {image_path} is not a valid BSON string.")
        return

    # Write the dictionary to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(metadata_dict, json_file, indent=4)

 
