**BRC-420-69 Ordinal Inscriptions**

BRC-420-69 is a new protocol for Ordinal Inscriptions on the Bitcoin blockchain. This Python-powered protocol provides a method of cryptographically storing an image with embedded metadata as an Ordinal that is private, immutable, secure, allows for delayed reveals of ordinals after minting, and contains verifiable metadata associated between the image and the collection metadata - ensuring long term provenance. This is also a standard that allows for onchain indexing btween the parent and children ordinals, allowing for fully permissionless Ordinals marketplace protocols that still display collection infromation and metadata.

The protocol involves a parent inscription (BRC-420) that contains a public JSON file. This JSON file indexes all of the child Ordinals by a combination of transaction ID and first-output as the most immutable data point for the indexing of Ordinals, and describes all of their other metadata, collection information, an AES encryption key, and the collection owner wallet(s). Because the transaction ID and first output cannot be known for the parent at the time of the child inscription creation, children will cross-reference the parent ordinal by satoshi number as the best available data point for the indexing within children ordinals.

The child inscription (BRC-69) consists of two SHA 256 hashes - one for the image and one for the metadata. With the AES key you can decrypt the hashes, which provides you with two base 64 strings: one base64 encoded bitmap image and one JSON containing base64 encoded metadata. The strings are further decoded into image and metadata, and the metadata is then steganographically embedded into the bitmap image.

The delayed reveal functionality allows for fair minting of ordinals to happen entirely on the Bitcoin blockchain. Ordinals can be listed on centralized marketplaces sight unseen, and they can be purchased there and revealed (upon parent inscription) after sellout. Only the holder of the parent information (and others with access to that information) would know the underlying files. 

Once inscribed, the parent inscription must remain in a designated owner wallet, or be sent to Satoshi's wallet to "renounce" the collection. This BRC-420 incription can be inscribed in an encrypted manner as well, to allow for less decentralized but more private decryption, or could even remain uninscribed to maintain more secrecy of the underlying inscription data (uninscribed "orphan" ordinals would also be appropriate for individual items not part of a collection). The privacy implications could be significant for any types of document that an individual might want inscribed onto the blockchain without it being publicly visible or known. 

Using cryptography as the basis for the inscribed ordinal is significant because it allows us to transcend what would ordinarily be the file size limits of ordinals WITHOUT "polluting" the Bitcoin blockchain. You can store significant amounts of data in a hash using the power of hash+encryption key. And by using base64 conversion of pixels, you can get exactly the same images - except bigger...and with steganography, you can embed metadata on those images. Two hashes can replace what would ordinarily be much larger file sizes. Once the parent inscription is inscribed, the data is immutably accessible and verifiable by checking the BRC-69 metadata against the BRC-420 metadata- provenance for Bitcoin Ordinals.

CRYPTOGRAPHY IS, ALWAYS HAS BEEN, AND ALWAYS WILL BE THE ANSWER. 

Disadvantages to this standard, especially currently, is that it's a lot of work to get all of the pieces of a collection together. I'm working on the tools for that. I would like to get to the point where anyone with the script can take an image library and properly formatted JSON + metadata table in a folder, aim a bash command at the folder, and get their collection hashes automatically. I believe the inscription of those hashes could be further automated but that is beyond my skill...I think. I look forward to seeing what others have to say/think about these ideas.    

Steps:

1. Assemble Parent (BRC-420) Collection JSON with all desired metadata. Identify satoshis of parent and child inscriptions using a satoshi indexer and include that information in the metadata of each.  
2. Next you will need to manually convert your desired visual output into a bitmap, and from there convert it into a base64 string. You can do the BMP to base64 conversion using the LibrarytoBMP script for all files in the chosen directory. 
3. Then, you will need to convert the metadata into a base64 and write it into a JSON.  You can do this using Metadata_Convert.  
4. Then using BRC69_EncryptStrings, you encrypt the base64 into two AES hashes using AES encryption. 
5. OrdinalMaker will take a designated JSON containing metadata as base64 alongside the base64 data for the images, and encrypt as a two separate hashes using AES encryption, writing them into a separate table. 
6. The paired AES hashes are your BRC-69 Ordinals. Inscribe all of your BRC-69 ordinals as strings using the format found in SampleBRC-69Ordinal. 
7. Incribe parent JSON file containing AES key and all metadata when you are ready to reveal the collection. 
8. Ensure accuracy and validity of all metadata, send parent ordinal to satoshi's wallet. 
9. Marketplaces, apps, websites, wallets and other readers will utilize BRC-69Decode+Embed to decode the AES hashes of individual ordinals using the (now public) key in a fully decentralized and permissionless way. [THIS IS NOT FUNCTIONAL YET!]

The BRC-69 Omni Decode + Embed Function does this:

Uses the AES key to decrypt the two hashes. 
Decodes the base64 strings into a BMP image and metadata.
Embeds metadata into the image using steganography.
Saves the resulting image. 
Writes the extracted metadata to a JSON file. 
Steganographically embeds the metadata into the image. Saves that output. 
  

Dependencies
This script depends on the following Python libraries:

  base64

  json

  PIL (Pillow)

  io

  stegano

  cryptography
  
  argparse
  
  pandas

Conclusion

The BRC-69 standard provides a robust method for taking image collections with associated metadata and inscribing them on the Bitcoin blockchain in a cryptographically secure manner, and ultimately decoding those inscriptions publicly with the inscription of the encryption key as a part of the parent ordinal. This allows for unique, private, identifiable, and verifiable inscriptions in the form of ordinals on the blockchain.

FOR ORDICORD COMPETITTION: ONLY SOME OF THESE PIECES ARE CURRENTLY WORKING AND NOT ALL OF THEM WILL END UP BEING PART OF THE FINAL PRODUCT. PLEASE FOCUS ON THIS DOCUMENT TO JUDGE MY PROJECT BUT FEE FREE TO TRY THEM. 
License
This project is licensed under the terms of the MIT license.

Please adjust the README as necessary based on your actual project details, licensing, usage instructions, and any additional information that you think will be helpful for users of your project.
