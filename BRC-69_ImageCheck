import base64
from PIL import Image
import io

BRC_69 = "your string here"  # Replace with the actual Base64 string

# Decode the Base64 string
decoded_data = base64.b64decode(BRC_69)

# Create a BytesIO object to wrap the decoded data
bytes_io = io.BytesIO(decoded_data)

# Open the image using PIL
image = Image.open(bytes_io)

# Display or save the image
image.show()  # Show the image using the default image viewer
# Alternatively, you can save the image to a file
# image.save('decoded_image.bmp')
