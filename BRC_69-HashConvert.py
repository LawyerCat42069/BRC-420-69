 import base64
import json
import bson
from PIL import Image
from io import BytesIO
from stegano import lsb
import packet

def decode_base64_to_image(BRC_69, output_path):
    # Decode base64 string
    decoded_data = base64.b64decode(BRC_69)

    # Convert decoded data to an image object
    img_data = BytesIO(decoded_data)
    image = Image.open(img_data)

    # Save the image as a bitmap
    image_path = "temp_image.bmp"
    image.save(image_path, format='BMP') 

    return image_path

def decode_and_embed_metadata(image_path, BRC_69_MD, output_image_path, output_json_path):
    # Decode the hidden metadata from base64
    decoded_metadata = base64.b64decode(BRC_69_MD)

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
    image_path = decode_base64_to_image(packet.BRC_69, 'C:\\path\\to\\your\\directory\\decoded_image.bmp')
    decode_and_embed_metadata(image_path, packet.BRC_69_MD, 'C:\\path\\to\\your\\directory\\final_image.bmp', 'C:\\path\\to\\your\\directory\\metadata.json')
