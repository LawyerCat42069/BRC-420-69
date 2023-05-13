import sys
import bson

def create_binary_equation_from_bson(file_path, base_number=990000000000000000000000000000):
    # Load the BSON data from file
    with open(file_path, 'rb') as file:
        bson_data = file.read()

    # Extract the binary data from the BSON
    binary_data = bson.loads(bson_data)

    # Convert binary data to a string of ones and zeros
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)

    # Convert binary string to a literal number
    literal_number = int(binary_string, 2)

    # Calculate the nearest exponent based on the literal number
    exponent = 0
    while base_number ** (exponent + 1) <= literal_number:
        exponent += 1

    # Calculate the result using the base number and exponent
    result = base_number ** exponent

    # Calculate the remainder necessary to match the literal number
    remainder = literal_number - result

    # Create the formula
    equation = f"{base_number}^{exponent}"

    if remainder > 0:
        equation += f" + {remainder}"

    return equation


if __name__ == '__main__':
    if len(sys.argv) > 1:
        bson_file = sys.argv[1]
    else:
        bson_file = input("Enter the BSON file path: ")

    base_number = 990000000000000000000000000000

    # Create the binary equation from BSON file (with specified base number)
    binary_equation = create_binary_equation_from_bson(bson_file, base_number)

    # Write the equation to a text file
    with open('binary_equation.txt', 'w') as file:
        file.write(binary_equation)
