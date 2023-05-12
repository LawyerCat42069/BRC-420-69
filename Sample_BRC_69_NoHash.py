import base64
import json
import bson
from PIL import Image
from io import BytesIO
from stegano import lsb

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

def decode_bson(base64_bson_metadata):
    # Decode the hidden metadata from base64
    decoded_metadata = base64.b64decode(base64_bson_metadata)

    # Convert the decoded metadata from BSON to a dictionary
    try:
        metadata_dict = bson.loads(decoded_metadata)
    except bson.InvalidBSON:
        print(f"Error: The hidden metadata is not a valid BSON string.")
        return None

    return metadata_dict

def embed_metadata(image_path, metadata_dict, output_path):
    # Convert the metadata dictionary to a JSON string
    metadata_json = json.dumps(metadata_dict)

    # Embed the metadata into the image using steganography
    secret_image = lsb.hide(image_path, metadata_json)
    secret_image.save(output_path)
