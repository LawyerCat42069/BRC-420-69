import os
import base64
import json
import argparse
import pandas as pd


def read_metadata_from_csv(csv_path):
    df = pd.read_csv(csv_path)
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

def main(csv_path):
    # Read metadata from the CSV file
    metadata_list = read_metadata_from_csv(csv_path)

    # Save metadata as JSON
    save_metadata_as_json(metadata_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert metadata from CSV to JSON')
    parser.add_argument('--csv', metavar='csv', default='metadata.csv', help='path to the CSV file (default: metadata.csv)')
    args = parser.parse_args()

    # Execute the main function with the provided CSV path
    main(args.csv)