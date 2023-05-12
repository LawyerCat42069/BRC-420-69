**BRC-420-69 Ordinal Inscriptions**

BRC-69 is a new standard for Ordinal Inscriptions on the Bitcoin blockchain. This Python script provides a method of cryptographically storing an image with embedded metadata on the Bitcoin blockchain as a Bitcoin ordinal.

The overall scheme involves a parent inscription (BRC-420) that contains a salt-encrypted JSON file. This JSON file indexes all of the child scripts by their Satoshi number and describes all of their metadata. The child inscription consists of two SHA 256 hashes - one for the image and one for the metadata. With the Salt key you can decrypt the hashes, which provides you with two base 64 strings: one encoded bitmap image and one BSON containing metadata.  

Steps:
Assemble Parent (BRC-420) Collection JSON with all desired metadata. Identify satoshis of parent and child inscriptions and include that information in the metadata of each.  
Next you will need to convert your desired visual output into a bitmap, and from there convert it into a base64 string. 
Then, you will need to convert the metadata into a BSON that is then converted into a separate base64 string.   

Then using BRC69_EncryptStrings, you encrypt the base64 into two AES hashes using AES encryption. 

The BRC-69 Omni Decode + Embed Function does this:

Uses the AES key to decrypt the two hashes. 
Decodes the base64 strings into an image and metadata.
Embeds metadata into the image using steganography.
Saves the resulting image.
Extracts the metadata from the image.
Writes the extracted metadata to a JSON file. 

The BRC-420 

Usage: Replace <Your_Base64_String_Here> with your actual base64 string that encodes an image. In the metadata_dict, replace <value> and <totalsize> with your actual metadata values. The metadata must be in valid JSON format.

Example:

python
    
Copy code
    
metadata_dict = {
    
    "Token Designation": "BRC-69",
    
    "Satoshi Number": "1234567887654321",
    
    "Parent Satoshi Number": "8765432112345678",
    
    "Collection Name": "My Collection",
    
    "Collection Size": "50",
    
    "Collection Number": "1/50",
    
    "Background": "Blue",
    
    "Body": "Warrior",
    
    "Face": "Happy",
    
    "Head": "Centurion Helm",
    
    "Neck": "None",

    "Waist": "Grenade Belt",

    "Back": "Jetpack",

    "Held": "Futuristic Laser Gun"
}

Metadata is first converted to binary using Metadata-BinaryConvert.py then decoded upon execution of the decoder by a marketplace/wallet/app/website. 
    
Please ensure you have installed all necessary Python libraries before running the script.

Make sure the BRC-69.py file is located in the same directory as your decoder script (main.py or whatever the filename is). Adjust the path in the loader line if necessary.

Dependencies
This script depends on the following Python libraries:

base64
json
PIL (Pillow)
io
stegano
Conclusion
The BRC-69 standard provides a robust method for embedding and extracting metadata from images stored on the Bitcoin blockchain. This allows for unique, identifiable, and verifiable inscriptions in the form of ordinals on the blockchain.

License
This project is licensed under the terms of the MIT license.

Please adjust the README as necessary based on your actual project details, licensing, usage instructions, and any additional information that you think will be helpful for users of your project.
