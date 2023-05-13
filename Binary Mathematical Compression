import math

def create_binary_equation(integer_value, base_number):
    # Find the logarithm of the integer value with the given base
    exponent = math.log(integer_value, base_number)

    # Calculate the nearest whole exponent that does not exceed the integer value
    exponent = math.floor(exponent)

    # Calculate the result using the base number and exponent
    result = base_number ** exponent

    # Calculate the remainder necessary to match the integer value
    remainder = integer_value - result

    # Create the formula
    equation = f"{base_number}^{exponent}"

    if remainder > 0:
        equation += f" + {remainder}"

    return equation


# Example usage
integer_value = 123456789
base_number = 21000000

# Create the binary equation
binary_equation = create_binary_equation(integer_value, base_number)

# Write the equation to a text file
with open('binary_equation.txt', 'w') as file:
    file.write(binary_equation)
