**BRC-420-69 Ordinal Inscriptions**
 
What if most of our Ordinals looked like this:

    BRC-69
  
    Collection Name: Collection of Ordinals

      Collection Image Satoshi number: XXXXXXXXXXXXXXXXX
    
      Item: Item No. / Collection Size  
    
    Parent wallet address: bc1qqah90veaaxrcee3hwlxfgucha8npcgp0nzruse 
     
      Parent Token Designation: BRC-420  
   
      Parent Satoshi Number: XXXXXXXXXXXXXXXXX
      
    
    Child Satoshi Number:XXXXXXXXXXXXXXXXX
    
        Child file type: JPEG  
        
    
    File Password Cipher: LjuGDb4MyvrCeSVj4Ia2LftJpT5wq51pkSqKKwjEm5I= [if desired] 
    
    
    Terms and Conditions txid/io [if applicable]:
        
        Terms and Conditions Satoshi Number [if applicable]:  
        
        Terms and Conditions Auth Wallet Address [if applicable]:
 
 The Parent Ordinal would consist of the following metadata:
        
       BRC-420 

         File type: JSON

         Collection Name: Collection of Ordinals
        
         Collection Description: This is a collection of Ordinals.
        
         Collection Image Satoshi Number: XXXXXXXXXXXXXXXXX

         Collection Image txid/io: XXXXXXXXXXXXXXXXX

        
        Parent Wallet Address: bc1qqah90veaaxrcee3hwlxfgucha8npcgp0nzruse
        
           Parent Satoshi Number: XXXXXXXXXXXXXXXXX
           
        
        Cipher Key [optional if child has encrypted pw]: Purrivate123456!
        
        
        Child File Type: JPEG 
         
         
        Terms and Conditions Auth Wallet Address [if applicable]:
          
          Terms and Conditions txid/io [if applicable]:
        
          Terms and Conditions Satoshi Number [if applicable]:  
         
         
        Table of collection metadata with references to each child satoshi by satoshi number as well as txid/io (the most immutable data point for an inscription). 
         
         
BRC-420-69 is a new protocol for Ordinal Inscriptions on the Bitcoin blockchain. This Python-powered protocol provides a method of cryptographically storing files with embedded metadata as an Ordinal that is private, immutable, secure, allows for delayed reveals of ordinals after minting, and contains verifiable metadata associated between the image and the collection metadata - ensuring long term provenance. This is also a standard that allows for onchain indexing btween the parent and children ordinals, allowing for fully permissionless Ordinals marketplace protocols that still display collection information and metadata.

The protocol involves a parent inscription (BRC-420) that contains a public JSON file. This JSON file indexes all of the child Ordinals by a combination of transaction ID and first-output as the most immutable data point for the indexing of Ordinals, and describes all of their other metadata, collection information, an AES encryption key [if applicable], and the collection owner wallet(s). Because the transaction ID and first output cannot be known for the parent at the time of the child inscription creation, children will cross-reference the parent Ordinal by satoshi number as the best available data point for the indexing within children ordinals.

The child inscription (BRC-69) consists of the necessary metadata specified above steganogrpahically embedded into either the file itself or a compressed file, depending on the needs and desires of the inscriber. NOTE: TESTING IS REQUIRED TO DETERMINE THE EXTENT TO WHICH THESE BYTES CAN BE EMBEDDED WITHOUT ALTERING COMPRESSED FILE CONTENTS. With the key you can decrypt the cipher, which gives you the password for the compressed file. The strings are further decoded into file and metadata, and the metadata is then steganographically embedded into the output file. The vision is that an ordinals reader will automatically pull the key from the BRC-420, decrypt the cipher, extract only the specified file type, and save it as the appropriate file type as designated in the BRC-420 in a sandbox environment used for display/ux. THIS COULD APPLY TO A MULTITUDE OF FILE TYPES. SO LONG AS THE PROTOCOL FOR ENSURING PROVENANCE OF THE PARENT ORDINAL IS LEGITIMATE, AND A SANDBOX ENVIRONMENT IS USED BY THE VIEWER APPLICATION, THE UNDERLYING FILE SHOULD BE SAFE TO EXTRACT IN THIS WAY.  

The delayed reveal functionality allows for fair minting of ordinals to happen entirely on the Bitcoin blockchain. Ordinals can be listed on centralized marketplaces sight unseen, and they can be purchased there and revealed (upon parent inscription) after sellout. Only the holder of the parent information (and others with access to that information) would know the underlying files. 

Once inscribed, the parent inscription must remain in a designated owner wallet, or be sent to Satoshi's wallet to "renounce" the collection. This BRC-420 incription can be inscribed in an encrypted manner as well, to allow for less decentralized but more private decryption, or could even remain uninscribed to maintain more secrecy of the underlying inscription data (uninscribed "orphan" ordinals would also be appropriate for individual items not part of a collection). The privacy implications could be significant for any types of document that an individual might want inscribed onto the blockchain without it being publicly visible or known.
 
Disadvantages to this standard, especially currently, is that it's a lot of work to get all of the pieces of a collection together. I'm working on the tools for that. I would like to get to the point where anyone with the script can take an file library and properly formatted JSON + metadata table in a folder, aim a bash command at the folder, and get their collection hashes automatically. I believe the inscription of those hashes could be further automated but that is beyond my current knowledge/skill. I look forward to seeing what others have to say/think about these ideas. Additionally another disadvantage is that the complication of decryption means that individuals will need to rely on readers in wallets, websites, marketplaces, and other applications in order to make the ordinal enjoyable in the traditional way. 

**Where does this go?** 

An actual web3. One that does not depend on web2 infrastructure to exist in any way, shape or form. Let's look at it from the 30,000 foot perspective:

Any file that can be compressed and inscribed can be authenticated and viewed using information that is entirely onchain. All you need is the key and the proper reading application to view the image. You can put dapps pieces (including such a reader) into files that contain executable code and cross-reference them with each other using inscription metadata. You could also inscribe compressed webpages - securing your HTML code with the power of the bitcoin blockchain and the AES/MD5 hash (really, TLS is an option here too). Webpages would likely require a different protocol entirely with similar provenance standards. You can inscribe html that calls to other inscriptions to display media or execute dapps, and can only be decompressed and read with the encryption key, which can be public or private. And once it is on the blockchain, it's there forever. The html can also call to data offchain. Permanent webhosting on the bitcoin blockchain and on your satoshis. Updating the website and hosting that only costs you inscription fees, and very small ones at that because HTML does not take up huge amounts of byte space. 


You could make it such that a terminal with bash, python & java with a full compliment, bitcoin core, inscription wallets, and an internet connection is capable of executing all of this in a sandbox environment (bash inscribable) with an amnesiac cache (inscribable). You can inscribe By doing this and using the BRC420-69 protocol and ensuring that the ordinals in question reside in the owner wallet or satoshi's wallet, this would be a very secure environment for the execution of dapps, viewing of websites, and many other applications. You can travel the world and access everything with nothing more than your seed phrases, any nonpublic encryption keys and a qualifying terminal. 

Is this complicated? Yes, but the complicated aspects can be automated and drastically simplified from a UX perspective. I am imagining a future where it doesn't matter if the government "shuts off the internet" as long as the Bitcoin network is operational. Node servers, node hosts. No gods, no masters.   

The next thing I would add is that this protocol is a tool with potential for positive or negative use cases, so I encourage any development on this protocol to keep in mind ways we can integrate best practices to mitigate any potential harm. I don't see alternatives to that which are fully decentralized, but distributed authority systems could make those alternatives more trustworthy.    

MATH AND CRYPTOGRAPHY IS, ALWAYS HAS BEEN, AND ALWAYS WILL BE THE ANSWER. 

Steps:

1. Assemble Parent (BRC-420) Collection JSON with all desired metadata and files for the collection. 
2. Compress the files. 
3. Then, you will need to setganogrpahically embed the metadata onto the compressed file. 
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
