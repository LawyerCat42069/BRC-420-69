**BRC-420-69 Ordinal Inscriptions**

BRC-69 is a new standard for Ordinal Inscriptions on the Bitcoin blockchain. This Python script provides a method of cryptographically storing an image with embedded metadata on the Bitcoin blockchain as a Bitcoin ordinal.

The overall scheme involves a parent inscription (BRC-420) that contains a salt-encrypted JSON file. This JSON file indexes all of the child scripts by their Satoshi number and describes all of their metadata. The child inscription consists of two SHA 256 hashes - one for the image and one for the metadata. With the Salt key you can decrypt the hashes, which provides you with two base 64 strings: one encoded bitmap image and one BSON containing metadata.  

Steps:

1. Assemble Parent (BRC-420) Collection JSON with all desired metadata. Identify satoshis of parent and child inscriptions and include that information in the metadata of each.  
2. Next you will need to convert your desired visual output into a bitmap, and from there convert it into a base64 string. You can do this using the LibrarytoBMP script for all files in the chosen directory. 
3. Then, you will need to convert the metadata into a BSON that is then converted into a separate base64 string.  You can do this using Metadata_BSON_Convert.  
4. Then using BRC69_EncryptStrings, you encrypt the base64 into two AES hashes using AES encryption. 
5. The AES hashes are your BRC-69 Ordinal. Inscribe all of your BRC-69 ordinals. 
6. Incribe parent JSON file containing AES key and all metadata. 
7. Ensure accuracy and validity of all metadata, send parent ordinal to satoshi's wallet. 
8. Marketplaces, apps, websites, wallets and other readers 

The BRC-69 Omni Decode + Embed Function does this:

Uses the AES key to decrypt the two hashes. 
Decodes the base64 strings into an image and metadata.
Embeds metadata into the image using steganography.
Saves the resulting image. 
Writes the extracted metadata to a JSON file. 
Steganographically embeds the metadata into the image. 
  

Dependencies
This script depends on the following Python libraries:

base64
json
PIL (Pillow)
io
stegano
cryptography


Conclusion
The BRC-69 standard provides a robust method for embedding and extracting metadata from images stored on the Bitcoin blockchain. This allows for unique, private, identifiable, and verifiable inscriptions in the form of ordinals on the blockchain.

License
This project is licensed under the terms of the MIT license.

Please adjust the README as necessary based on your actual project details, licensing, usage instructions, and any additional information that you think will be helpful for users of your project.
