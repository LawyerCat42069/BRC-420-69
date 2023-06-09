import os
import base64
import json
import argaprse

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

def main(folder_path):
    # Convert images to Base64 and create the JSON data
    base64_data = folder_to_base64_json(folder_path)

    # Save the Base64 data as JSON in the same folder
    save_base64_json(base64_data, folder_path)

if __name__ == '__main__':
    # Prompt for the folder path containing the BMP images
    folder_path = input('Enter the folder path: ')

    # Execute the main function with the provided folder path
    main(folder_path)
