import os
import base64
import json
import argparse
import pandas as pd


def read_metadata_from_file(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        df = pd.read_json(file_path)
    else:
        print('Unsupported file type.')
        return None

    metadata_list = []
    for _, row in df.iterrows():
        metadata_dict = {}
        for column, value in row.items():
            metadata_dict[column] = value
        encoded_metadata = encode_metadata_as_base64(metadata_dict)
        metadata_list.append(encoded_metadata)
    return metadata_list


def encode_metadata_as_base64(metadata):
    encoded_metadata = {}
    for key, value in metadata.items():
        encoded_value = base64.b64encode(str(value).encode('utf-8')).decode('utf-8')
        encoded_metadata[key] = encoded_value
    return encoded_metadata


def save_metadata_as_json(metadata_list):
    json_file_path = 'metadata.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(metadata_list, json_file, indent=4)


def main(file_path):
    # Read metadata from the file
    metadata_list = read_metadata_from_file(file_path)

    # Check if metadata_list is not None (i.e., file reading was successful)
    if metadata_list is not None:
        # Save metadata as JSON
        save_metadata_as_json(metadata_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert metadata from file to JSON')
    parser.add_argument('--file', metavar='file', default='metadata.csv', help='path to the file (default: metadata.csv)')
    args = parser.parse_args()

    # Execute the main function with the provided file path
    main(args.file)
