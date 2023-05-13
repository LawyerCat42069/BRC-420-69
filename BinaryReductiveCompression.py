import sys
import bson

def find_efficient_representation(binary_data):
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    exponent = binary_string.index('1') + len(binary_string) - 1
    remainder = int(binary_string, 2) - 2 ** (exponent)
    representation = f"2^{exponent} + {remainder}"
    return representation

def main():
    if len(sys.argv) > 1:
        bson_file_path = sys.argv[1]
    else:
        bson_file_path = input("Enter the BSON file path: ")

    try:
        with open(bson_file_path, 'rb') as file:
            binary_data = bson.loads(file.read())

        representation = find_efficient_representation(binary_data)
        print(f"The efficient mathematical representation for the binary data is: {representation}")
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()
