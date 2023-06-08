# this script takes a folder of numbered images (number is the file name) and a JSON of metadata with a "Number" trait and embeds the corresponding metadata into the images

import os
import json
from stegano import lsb

# Prompt the user to enter the image folder path
image_folder = input("Enter the path to the folder containing numbered images: ")

# Prompt the user to enter the JSON file path
metadata_file = input("Enter the path to the JSON file containing metadata: ")

# Load the metadata from the JSON file
with open(metadata_file, "r") as f:
    metadata = json.load(f)

# Embed metadata into the corresponding images
for entry in metadata:
    number = entry["Number"]
    image_path = os.path.join(image_folder, f"{number}.png")
    metadata_to_embed = json.dumps(entry)  # Convert metadata to string (modify as per your JSON structure)
    embedded_image_path = image_path.replace(".png", "_embedded.png")

    # Embed metadata using stegano
    secret = lsb.hide(image_path, metadata_to_embed)
    secret.save(embedded_image_path)

    print(f"Embedded metadata into {embedded_image_path}")
