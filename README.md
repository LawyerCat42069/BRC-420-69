**BRC-420-69 Ordinal Inscriptions**
 
What if our Ordinals looked like this:

    BRC-69
  
    Collection Name: Collection of Ordinals
    
    Item: Item No. / Collection Size
    
    Parent file type:
    
    Child file ype: 
    
    Parent wallet address: bc1qqah90veaaxrcee3hwlxfgucha8npcgp0nzruse
    
    Parent Satoshi Number: XXXXXXXXXXXXXXXXX
    
    Child Satoshi Number:XXXXXXXXXXXXXXXXX
    
    Parent Token Designation: BRC-420  
    
    Image Cipher: Encrypted compressed file pw
    
    Metadata Cipher: Encrypted compressed file pw 
 
 The Parent Ordinal would consist of the following metadata:
        
       BRC-420 

        File type: JSON

        Collection Name: Collection of Ordinals
        
        Collection Description: This is a collection of Ordinals
        
        Parent Wallet Address: bc1qqah90veaaxrcee3hwlxfgucha8npcgp0nzruse
        
        Parent Satoshi Number: XXXXXXXXXXXXXXXXX
        
        Cipher Key
        
        Child File Type: JPEG
        
        Collection Image Satoshi Number:

        Collection Image txid/io:

        Terms and Conditions txid/io (if applicable):
        
        Terms and Conditions txid/io (if applicable):  
        
        Table of collection metadata with references to each child satoshi by satoshi number as well as txid/io (the most immutable data point for an inscription). 
        
        
        

BRC-420-69 is a new protocol for Ordinal Inscriptions on the Bitcoin blockchain. This Python-powered protocol provides a method of cryptographically storing an image with embedded metadata as an Ordinal that is private, immutable, secure, allows for delayed reveals of ordinals after minting, and contains verifiable metadata associated between the image and the collection metadata - ensuring long term provenance. This is also a standard that allows for onchain indexing btween the parent and children ordinals, allowing for fully permissionless Ordinals marketplace protocols that still display collection information and metadata.

The protocol involves a parent inscription (BRC-420) that contains a public JSON file. This JSON file indexes all of the child Ordinals by a combination of transaction ID and first-output as the most immutable data point for the indexing of Ordinals, and describes all of their other metadata, collection information, an AES encryption key, and the collection owner wallet(s). Because the transaction ID and first output cannot be known for the parent at the time of the child inscription creation, children will cross-reference the parent Ordinal by satoshi number as the best available data point for the indexing within children ordinals.

The child inscription (BRC-69) consists of the parent satoshi number and two ciphers - one for the image and one for the metadata. With the key you can decrypt the ciphers, which provides you with two binary strings: one file and one JSON containing base64 encoded metadata. The strings are further decoded into image and metadata, and the metadata is then steganographically embedded into the bitmap image.

The delayed reveal functionality allows for fair minting of ordinals to happen entirely on the Bitcoin blockchain. Ordinals can be listed on centralized marketplaces sight unseen, and they can be purchased there and revealed (upon parent inscription) after sellout. Only the holder of the parent information (and others with access to that information) would know the underlying files. 

Once inscribed, the parent inscription must remain in a designated owner wallet, or be sent to Satoshi's wallet to "renounce" the collection. This BRC-420 incription can be inscribed in an encrypted manner as well, to allow for less decentralized but more private decryption, or could even remain uninscribed to maintain more secrecy of the underlying inscription data (uninscribed "orphan" ordinals would also be appropriate for individual items not part of a collection). The privacy implications could be significant for any types of document that an individual might want inscribed onto the blockchain without it being publicly visible or known.

**HOW IS THIS POSSIBLE?** 

I am working on a compression table/formula that will take raw binary data and express it down to the simplest mathematical formula (base^exponent+int=X, where x=the literal numeric value of a given file's binary string as an integer - not using traditional binary addition). The compression table substitutes letters/symbols for very large numbers which will enable reduction of the large (not arbitrarily large, but very large) binary value to a very short string. Theoretically, just by doing the math one will replicate the initial binary value down to under 1kb. The compression table and compression/decompression scripts can be publicly published on the blockchain to allow for easy, on-chain translation of files into BRC (Binary-Reductive-Compression). It should be noted however, that BRC does require a fair amount of computing power to accomplish the intial calculation of string value or translate it back - the larger the file, the more computing power required. Because of the blockchain based structure, the burden of computing/processing and storage falls on the end user. Theoretically, by referencing the compression table (likely contained in a parent BRC-420 along with provenance information consistent with the protocol), one can achieve lossless compression of binary data, and then encrypt that data for transmission on the blockchain. The compression script will turn an ordinal file and its metadatainto binary data into a simple mathematical formula, which can then be encrypted using traditional encryptionry methods and transmitted on the blockchain as a small ordinal. By referncing the underlying file's BRC-420 parent, the decoding script can identify and save the binary output as the appropthe appropriate file type.        

Using cryptography as the basis for the inscribed ordinal is significant because it allows us to transcend what would ordinarily be the file size limits of ordinals. You can store significant amounts of data in a hash using the power of hash+encryption key. And by using base64 conversion of pixels, you can get exactly the same images - except bigger...and with steganography, you can embed metadata on those images. Two hashes and slightly more arbitrary data can replace what would ordinarily be much larger file sizes. Once the parent inscription is inscribed, the data is immutably accessible and verifiable by checking the BRC-69 metadata against the BRC-420 metadata- ensuring provenance for Bitcoin Ordinals. And because the parent inscription references the children by transaction ID and first output, that point of reference is truly immutable and will always point to the actual child inscriptions. 

MATH AND CRYPTOGRAPHY IS, ALWAYS HAS BEEN, AND ALWAYS WILL BE THE ANSWER. If you don't burn the bitcoin punk that you burned your eth cryptopunk for, in order to obtain the BRC-69 Punk, what are you even doing with your life? 

Disadvantages to this standard, especially currently, is that it's a lot of work to get all of the pieces of a collection together. I'm working on the tools for that. I would like to get to the point where anyone with the script can take an file library and properly formatted JSON + metadata table in a folder, aim a bash command at the folder, and get their collection hashes automatically. I believe the inscription of those hashes could be further automated but that is beyond my current knowledge/skill. I look forward to seeing what others have to say/think about these ideas. Additionally another disadvantage is that the complication of decryption means that individuals will need to rely on readers in wallets, websites, marketplaces, and other applications in order to make the ordinal enjoyable in the traditional way. 

**Where does this go?** 

An actual web3. One that does not depend on web2 infrastructure to exist in any way, shape or form. Let's look at it from the 30,000 foot perspective:

We can inscribe arbitrary amounts of data onchain in small text or .py files using the power of encryption. You can store entire coding libraries cryptographically along with the encryption key in the same hash to make them readily accessible. You could inscribe a full size, high resolution Mona Lisa on one hash. All you need is the key and the proper reading application to view the image. You can put dapps pieces (including such a reader) into files that contain executable code and cross-reference them with each other using inscription metadata. You could also embed arbitrary amounts of html code into an encrypted hash and store large webpages on the bitcoin blockchain - securing your HTML code with the power of the bitcoin blockchain and the AES/MD5 hash (really, TLS is an option here too). You can inscribe html that calls to other inscriptions to display media or execute dapps, and can only be read with the encryption key, which can be public or private. You could make it such that a terminal with bash, python with a full compliment, bitcoin core, inscription wallets, and an internet connection is capable of executing all of this. By using the BRC420-69 protocol and ensuring that the ordinals in question reside in the owner wallet or satoshi's wallet, this would be a very secure environment for the execution of dapps, viewing of websites, and many other applications. You can travel the world and access everything with nothing more than your seed phrases, any nonpublic encryption keys and a qualifying terminal. The only thing I would add is that this protocol is a tool with potential for positive or negative use cases, so I encourage any development on this protocol to keep in mind ways we can integrate best practices to mitigate any potential harm.   

Steps:

1. Assemble Parent (BRC-420) Collection JSON with all desired metadata. Identify satoshis of parent and child inscriptions using a satoshi indexer and include that information in the metadata of each.  
2. Next you will need to manually convert your desired visual output into a bitmap, and from there convert it into a base64 string. You can do the BMP to base64 conversion using the BMPConvert script for all files in the chosen directory. 
3. Then, you will need to convert the metadata into a base64 and write it into a JSON.  You can do this using Metadata_Convert.  
4. Then using BRC69_EncryptStrings, you encrypt the base64 into two AES hashes using AES encryption. 
5. OrdinalMaker will take a designated JSON containing metadata as base64 alongside the base64 data for the images, and encrypt as a two separate hashes using AES encryption, writing them into a separate table. 
6. The paired AES hashes are your BRC-69 Ordinals. Inscribe all of your BRC-69 ordinals as strings using the format found in SampleBRC-69Ordinal. 
7. Incribe parent JSON file containing AES key and all metadata when you are ready to reveal the collection. 
8. Ensure accuracy and validity of all metadata, send parent ordinal to satoshi's wallet. 
9. Marketplaces, apps, websites, wallets and other readers will utilize BRC-69Decode+Embed to decode the AES hashes of individual ordinals (of numerous file types) using the (now public) key in a fully decentralized and permissionless way. [THIS IS NOT FUNCTIONAL YET!] The decoding script ideally long term will be written to process mutliple file types, but if it processes applications it must check them against an BRC-420 containing an approved list of secure dApp ordinals and file types before executing any script. (Ideally that list is managed via largely distributed multisignature and contains multiple valid owner wallets, so that it can be passed on to a new owner quickly if need be. Perhaps that could be further decentralized but I'm not there yet.) If the file does not match the list of approved file types AND/OR does not exist in the BRC-420 metadata of the approved list of dapps, then the decoder app should immediately delete the file and self-terminate, requiring the end user to re-instigate the app. This does create a point of centralization but nothing would preclude the existence of a decoder app that breaks this protocol. I just don't think that would be secure. 

The BRC-69 Omni Decode + Embed Function does this:

Uses the AES key to decrypt the two hashes. 
Decodes the base64 strings into a BMP image and metadata.
Embeds metadata into the image using steganography.
Saves the resulting image. 
Writes the extracted metadata to a JSON file. 
Steganographically embeds the metadata into the image. Saves that output.  
Dependencies
This script depends on the following Python libraries: 
  base64, 
  json, 
  PIL (Pillow), 
  io, 
  stegano, 
  cryptography, 
  argparse, 
  pandas,


**Conclusion**

The BRC-420/69 standard provides a robust method for taking file collections with associated metadata and inscribing them on the Bitcoin blockchain in a cryptographically secure manner, and ultimately decoding those inscriptions publicly with the inscription of the encryption key as a part of the parent ordinal. This allows for unique, secure, private, identifiable, and verifiable inscriptions in the form of ordinals on the blockchain. 

FOR ORDICORD COMPETITTION: ONLY SOME OF THESE PIECES ARE CURRENTLY WORKING AND NOT ALL OF THEM WILL END UP BEING PART OF THE FINAL PRODUCT. PLEASE FOCUS ON THIS DOCUMENT TO JUDGE MY PROJECT BUT FEE FREE TO TRY THEM. 

License:  
This project is licensed under CC0, do whatever you want.
