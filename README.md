**BRC-420-69 Ordinal Inscriptions:** 

**A Standard for Secure File Storage, Authentication, and Management on the Bitcoin Blockchain**
 
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
        
        Compression & Method: .zip
        
    
    File Password Cipher: LjuGDb4MyvrCeSVj4Ia2LftJpT5wq51pkSqKKwjEm5I= [if desired] 
    
    
    Terms and Conditions txid/io [if applicable]:
        
        Terms and Conditions Satoshi Number [if applicable]:  
        
        Terms and Conditions Auth Wallet Address [if applicable]:
        
    **Ordinal.filetype or Ordinal.zip**    
 
 The Parent Ordinal would be a JSON consisting of the following metadata:
        
       BRC-420  

         Collection Name: Collection of Ordinals
        
         Collection Description: This is a collection of Ordinals.
        
         Collection Image Satoshi Number: XXXXXXXXXXXXXXXXX

         Collection Image txid/io: XXXXXXXXXXXXXXXXX

        
        Parent Wallet Address: bc1qqah90veaaxrcee3hwlxfgucha8npcgp0nzruse
        
           Parent Satoshi Number: XXXXXXXXXXXXXXXXX
           
        
        Cipher Key [optional if child has encrypted pw]: Purrivate123456!
        
        
        Child File Extension: .jpg
           Children Compression file type [if needed]: .zip  
         
         
        Terms and Conditions Auth Wallet Address [if applicable]:
          
          Terms and Conditions txid/io [if applicable]:
        
          Terms and Conditions Satoshi Number [if applicable]:  
         
         
        **Table of collection metadata with references to each child satoshi by satoshi number as well as txid/io (the most immutable data point for an inscription).** 
         
         
BRC-420-69 is a new protocol for Ordinal Inscriptions on the Bitcoin blockchain. This protocol provides a method of storing files with embedded metadata as an Ordinal that is potentially private, immutable, secure, allows for delayed reveals of ordinals after minting, and contains verifiable metadata associated between the child file and the parent collection metadata - ensuring long term provenance. This is also a standard that allows for onchain indexing btween the parent and children ordinals, allowing for fully permissionless Ordinals marketplace protocols that still display collection information and metadata. Infrastructure is needed for all of this to work in a seamless way, but I have started planning that and with my limited skills I am putting together parts of the whole. 

The protocol involves a parent inscription (BRC-420) that contains a public JSON file. This JSON file indexes all of the child Ordinals by a combination of transaction ID and first-output as the most immutable data point for the indexing of Ordinals, and describes all of their other metadata, collection information, an AES encryption key [if applicable] of the password for the compressed ordinal on the child satoshi (if compressed), and the collection owner wallet(s). 

The child inscription (BRC-69) consists of the necessary metadata specified above steganogrpahically embedded into both the file itself and a compressed/zip file (if used), depending on the needs and desires of the inscriber. Because the transaction ID and first output cannot be known for the parent at the time of the child inscription creation, children will cross-reference the parent Ordinal by satoshi number as the best available data point for the indexing within children ordinals.

The significance of using compression is two-fold: It allows us to inscribe more bytes of information into a single inscription, enabling significantly larger file inscriptions, and it also 

NOTE: TESTING IS REQUIRED TO DETERMINE THE EXTENT TO WHICH THESE BYTES CAN BE EMBEDDED WITHOUT ALTERING COMPRESSED FILE CONTENTS. With the key you can decrypt the cipher, which gives you the password for the compressed file. The strings are further decoded into file and metadata, and the metadata is then steganographically embedded into the output file. The vision is that an ordinals reader will automatically pull the key from the BRC-420, decrypt the cipher, extract only the specified file type, and save it as the appropriate file type as designated in the BRC-420 in a sandbox environment used for display/ux. This could apply to a multitude of file types. So long as the process for ensuring provenance of the parent/child pair is legitimate, and a properly constructed environment is used by the sandbox application, the underlying files shoudl be safe to extract and use in this way.

SUB-NOTE: THE SECURITY OF OF ANY ENCRYPTED PASSWORD IS IN LARGE PART DEPENDENT ON THE LENGTH OF THE ENCRYPTED PASSWORD. PASSWORDS OF FILES ON THE BLOCKCHAIN ARE SUSCEPTIBLE TO BRUTE FORCE ATTACKS, SO ANY EFFORTS AT TRUE SECRECY MUST TAKE THIS INTO ACCOUNT.  

The delayed reveal functionality allows for fair minting of ordinals to happen entirely on the Bitcoin blockchain. Ordinals can be listed on centralized marketplaces sight unseen, and they can be purchased there and revealed (upon parent inscription) after sellout. Only the holder of the parent information (and others with access to that information) would know the underlying files. 

Once inscribed, the parent inscription must remain in a designated owner wallet, or be sent to Satoshi's wallet to "renounce" the collection. This BRC-420 incription can be inscribed in an encrypted manner as well, to allow for less decentralized but more private decryption, or could even remain uninscribed to maintain more secrecy of the underlying inscription data (uninscribed "orphan" ordinals would also be appropriate for individual items not part of a collection). The privacy implications could be significant for any types of document that an individual might want inscribed onto the blockchain without it being publicly visible or known.

**SWOT ANALYSIS**

   **Stengths:** I believe these are fairly indicated above. I think the greatest srength lies in the potential of onchain indexing. 
 
   **Weaknesses:** Disadvantages to this standard, especially currently, is that it's a lot of work to get all of the pieces of a collection together, which could be discouraging for use of the protocol. Figuring out sat #s in advance and targeting them specifically in advance is no easy task - but that is the price that must be paid for provenance as far as I can tell. Working on tools for that and would love help. I would like to get to the point where anyone with the script can take a file library and properly formatted JSON + metadata table in a folder, aim a bash command at the folder, generate the cipher and embed the metadata automatically, with minimal input. I believe the inscription of those hashes could be further automated if the target satoshi information is known but that is beyond my current knowledge/skill.  
   
Additionally another disadvantage of the compression/encryption is that the complication of decryption means that individuals will need to rely on readers in wallets, websites, marketplaces, and other applications in order to make the ordinal enjoyable in the traditional way. The complication of decompression of a strange file on the blockchain comes with security risks. The tools will need to be built, safely, and people will need to be convinced that this is worthwhile. However if these reader scripts and applications can be inscribed, they too could exist as dapps on the Bitcoin blockchain that can be easily accessed with the right starter data.  

The next thing I would add is that this protocol is a tool with potential for positive or negative use cases, so I encourage any development on this protocol to keep in mind ways we can integrate best practices to mitigate any potential harm. I don't see alternatives to that which are fully decentralized, but distributed authority systems could make those alternatives more trustworthy, or at least create a system of trusted resources by reference to their ordinal information such as dapps, websites, etc. People could rely on them or not as they chose, but I see value in a trustworthy source of information on which inscribed dapps and inscribed websties, in particular, are safe. Additionally could include an inscribed list (or multiple lists linked with metadata) of malicious or problematic inscriptions for decentralized protocols to optionally filter out such content. 

   **Opportunities:** It's a wide open field right now with Ordinals just becoming popular. Now is the time to set a strong standard that takes into account security, decentralized protocols (onchain indexing), and other standards to ensure secure, optimal use cases for the technology moving forward.

   **Threats:** Abuse of the protocol leading to a bad reputation is my primary concern here. Malware or other malicious/illegal files being inscribed and attempting to fool the protocol to create security or other threats to end users or the blockchain itself. Aside from that, the threats to this protocol are the same as the threats to Bitcoin itself.  

I look forward to seeing what others have to say/think about these ideas. 

**Where does this go?** 

An actual web3. One that does not need to depend on web2 infrastructure other than the series of tubes itself to exist in any way, shape or form. Let's look at it from the 30,000 foot perspective:

Any file that can be compressed and inscribed can be authenticated and viewed using information that is entirely onchain. All you need is the key (if needed) and the proper application to use the file, whatever it may be. You can put dapp  pieces (including such a reader) into files that contain executable code and cross-reference them with each other, daisy chain them, using inscription metadata. You could also inscribe compressed/protected webpages - securing your HTML code with the power strong password security and the AES/MD5 hash (really, TLS is an option here too). Webpages would likely require a different protocol entirely with similar provenance standards. You can inscribe html that calls to other inscriptions to display media or execute dapps, and can only be decompressed and read with the encryption key, which can be public or private. And once it is on the blockchain, it's there forever. The html can also call to data offchain. Permanent webhosting on the bitcoin blockchain and on your satoshis. Updating the website and hosting that only costs you inscription fees, and very small ones at that because HTML does not take up huge amounts of byte space. 
 
You could make it such that a terminal with bash, python & java with a full compliment, bitcoin core, inscription wallets, and an internet connection is capable of executing all of this in a sandbox environment (bash inscribable) with an amnesiac cache (inscribable). You can inscribe a BitcoinBrowser to make API calls to the blockchain or explaore the internet. By doing this in a sandbox environment with an amnesiac cache and using the BRC420-69 protocol to ensure that the ordinals in question reside in the owner wallet or satoshi's wallet, this would be a very secure environment for the execution of dapps, viewing of websites, and many other applications. You can travel the world and access everything with nothing more than your seed phrases, any nonpublic encryption keys and a qualifying terminal. 

**Is this too complicated?**

Possibly, definitely for some - but the complicated aspects can be automated and drastically simplified from a UX perspective. I am imagining a future where it doesn't matter if the government "shuts off the internet" as long as the Bitcoin network is operational. Node servers, node hosts. No gods, no masters. 

All you need is the information of the ordinal containing the sandbox enironment script and the same for the browser script, provided that the shell is able to explore the bitcoin blockchain. That plus your key(s) and you are off to the races. Of course some files will always be too big to inscribe, but those can be hosted in web2 and referenced by inscribed scripts (which can be updated via re-inscription) if need be. I am thinking the shell and browser reside in parent ordinals, which can be called and executed through the 420/69 or similar protocol by calling a child ordinal, validating the provenance of both through onchain indexing/cross-referencing of metadata. Distribution of satoshis can replace distribution of software in a sense, because without knowledge of the satoshi's information (which could also be protected by an encrypted cipher), they will not be able to readily access the underlying file.  

**Other downsides?**


INSCRIBER PROTOCOL:

1. Assemble Parent (BRC-420) Collection JSON with all desired metadata and files for the collection. 
2. Identify target satoshi of parent ordinal using a satoshi indexer, add that information to BRC-420 and individual child metadata.  
4. OPTIONAL: Choose a secure password for compressed files (delayed reveal, secrecy/privacy). 
5. OPTIONAL: Encrypt password using AES Encryption, note encryption key in BRC-420 table. Insert cipher into child ordinal metadata table. 
3. Steganographically embed the metadata into the files (automated ideally).   
7. OPTIONAL: Compress the Child Ordinal files.
8. OPTIONAL: Lock the Zip file using the chosen password.   
9. OPTIONAL: Then, you will need to steganogrpahically embed the Child Ordinal metadata onto the compressed files (also automated, same process).  
10. Inscribe all of the child ordinal files first, noting each satoshi number and txid/io. 
11. Complete the BRC-420 metadata table with the information from step 8, ensure completeness of metadata. 
12. Inscribe BRC-420 JSON file onto target parent ordinal.  
13. Ensure accuracy and validity of all metadata, send parent ordinal to satoshi's wallet if there is a desire to renounce the metadata. 

READER PROTOCOL:

1. Operate in a secure sandbox environment with access to bash/python/java/any other needed coding libraries and a basic web browser (or maybe one day, BitcoinBrowser), other file readers, any other security protocol we can think of. Maybe the shell script could also be inscribed. 

2. Always ensure provenance of parent/child pair, first check that parent is in an authorized wallet and that the satoshi numbers and file type metadata contained in both ordinals match the expected numbers and file types based on cross-referencing - compare txid/io to the child ordinal contents. If it does not match, delete file and display that "Ordinal cannot be displayed because it cannot be authenticated."  

3. Default display for any encrypted/compressed Orindal is the collection image as specified in the BRC-420. After ensuring provenance, check for compressed file. If yes, check for pw lock. If locked, check BRC-420 for line containing encryption key. If none, prompt user for Encryption Key. 

4. Using Encryption Key, decrypt file password from metadata. Unlock file, check file type against parent ordinal metadata. If file type does not match, clear directory and immediately terminate shell. 

5. Assuming file type matches, Check steganographically embedded metadata. If metadata does not match, clear directory and immediately terminate decoder.  

6. Assuming metadata matches, perform any needed security checks, If the compressed file fails the security check, clear directory and terminate shell.  

7. Extract/save the file to specified (temporary) directory for use, open appropriate reading application (ideally an authentic inscribed dapp), or opens the directory containing the downloaded file if no appropriate reader can be found within the shell. 
 
8. Reading application picks up on and displays all Child Ordinal metadata alongside the Child Ordinal file in an aesthetically pleasing manner.  
        
The decoding script ideally long term will be written to process mutliple file types, but if it processes applications it could check them against an BRC-420 containing an approved list of secure dApp ordinals and file types before executing any script. (Ideally that list is managed via largely distributed multisignature and contains multiple valid owner wallets, so that it can be passed on to a new owner quickly if need be. Perhaps that could be further decentralized but I'm not there yet.) If the file does not match the list of approved file types AND/OR does not exist in the BRC-420 metadata of the approved list of dapps, then the decoder app should immediately delete the file and self-terminate, requiring the end user to re-instigate the app. This does create a point of centralization but nothing would preclude the existence of a decoder app that breaks this protocol. I just don't think that would be secure. 

The BRC-69 Omni Decode + Embed Function does this currently:

Uses the AES key to decrypt the two hashes. 
Decodes the base64 strings into a BMP image and metadata.
Embeds metadata into the image using steganography.
Saves the resulting image. 
Writes the extracted metadata to a JSON file. 
Steganographically embeds the metadata into the image. Saves that output.  

This is outdated based on the protocol outlined above. Lots of this needs rewriting at this point. Might start fresh. 

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

The BRC-420/69 standard provides a robust method for taking file collections with associated metadata and inscribing them on the Bitcoin blockchain, potentially in a cryptographically secure manner, and ultimately decoding those inscriptions publicly with the inscription of the encryption key as a part of the parent ordinal. This allows for unique, secure, private, identifiable, and verifiable inscriptions in the form of ordinals on the blockchain. 

FOR ORDICORD COMPETITTION: ONLY SOME OF THESE PIECES ARE CURRENTLY WORKING AND NOT ALL OF THEM WILL END UP BEING PART OF THE FINAL PRODUCT. PLEASE FOCUS ON THIS DOCUMENT TO JUDGE MY PROJECT BUT FEE FREE TO TRY THEM. 

License:  
This project is licensed under CC0, do whatever you want.
