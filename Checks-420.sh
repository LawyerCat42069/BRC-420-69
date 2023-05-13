#!/bin/bash

# Read the data from the source file
SOURCE_FILE="source.json"
PARENT_SATOSHI_NUMBER=$(jq -r '.parentSatoshiNumber' "$SOURCE_FILE")
CHILD_SATOSHI_NUMBER=$(jq -r '.childSatoshiNumber' "$SOURCE_FILE")
FILE_CIPHER=$(jq -r '.fileCipher' "$SOURCE_FILE")
METADATA_CIPHER=$(jq -r '.metadataCipher' "$SOURCE_FILE")

# Function to prompt for the output directory
prompt_for_output_directory() {
    echo "Enter the output directory path:"
    read -r OUTPUT_DIRECTORY

    # Check if the directory exists
    if [[ ! -d "$OUTPUT_DIRECTORY" ]]; then
        echo "Output directory does not exist. Please enter a valid directory."
        prompt_for_output_directory
    fi
}
# Function to prompt for the encryption key
prompt_for_encryption_key() {
    echo "Enter the encryption key:"
    read -r ENCRYPTION_KEY
}

# Check if the encryption keys are available in the source file
if [[ $(jq '.encryptionKeys | length' "$SOURCE_FILE") -eq 0 ]]; then
    echo "Encryption keys not found in the source file."
    prompt_for_encryption_key
else
    # Extract the encryption keys from the source file
    ENCRYPTION_KEYS=$(jq -r '.encryptionKeys | @tsv' "$SOURCE_FILE")

    # Loop through the encryption keys
    while read -r ENCRYPTION_KEY; do
        # Decrypt the File Cipher using the Encryption Key
        DECRYPTED_FILE_CIPHER=$(echo "$FILE_CIPHER" | openssl enc -d -base64 -aes-256-cbc -pbkdf2 -pass "pass:$ENCRYPTION_KEY")

        # Decrypt the Metadata Cipher using the Encryption Key
        DECRYPTED_METADATA_CIPHER=$(echo "$METADATA_CIPHER" | openssl enc -d -base64 -aes-256-cbc -pbkdf2 -pass "pass:$ENCRYPTION_KEY")

        # Check if decryption was successful
        if [[ -n "$DECRYPTED_FILE_CIPHER" && -n "$DECRYPTED_METADATA_CIPHER" ]]; then
            # Display the extracted data
            echo "Decrypted File Cipher:"
            echo "$DECRYPTED_FILE_CIPHER"
            echo "Decrypted Metadata Cipher:"
            echo "$DECRYPTED_METADATA_CIPHER"

            # Save the decrypted File Cipher to a file
            echo "$DECRYPTED_FILE_CIPHER" > decrypted_file_cipher.txt
            echo "Decrypted File Cipher saved as decrypted_file_cipher.txt"

            # Save the decrypted Metadata Cipher to a JSON file
            echo "$DECRYPTED_METADATA_CIPHER" > decrypted_metadata_cipher.json
            echo "Decrypted Metadata Cipher saved as decrypted_metadata_cipher.json"

            break
        fi
    done <<< "$ENCRYPTION_KEYS"

    # If decryption failed, prompt for the encryption key
    if [[ -z "$DECRYPTED_FILE_CIPHER" || -z "$DECRYPTED_METADATA_CIPHER" ]]; then
        echo "Decryption failed with the available encryption keys."
        prompt_for_encryption_key
    fi
fi

# Set the transaction ID (TXID)
TXID="<transaction_id>"

# Fetch the raw transaction
RAW_TX=$(bitcoin-cli getrawtransaction $TXID)

# Decode the raw transaction
DECODED_TX=$(bitcoin-cli decoderawtransaction $RAW_TX)

# Extract the specific output by index (Parent Satoshi)
OUTPUT_PARENT=$(echo "$DECODED_TX" | jq ".vout[$PARENT_SATOSHI_NUMBER]")

# Extract the output script from the parent output
OUTPUT_PARENT_SCRIPT=$(echo "$OUTPUT_PARENT" | jq -r '.scriptPubKey.hex')

# Decode the script and check for inscribed data (Parent Data)
PARENT_DATA=$(echo "$OUTPUT_PARENT_SCRIPT" | xxd -r -p | awk '/OP_RETURN/ { print $2 }' | xxd -r -p)

# Display the extracted data
echo "Parent Data:"
echo "$PARENT_DATA"

# Extract the child Satoshi number from the Parent Data column
CHILD_SATOSHI_NUMBER_PARENT_DATA=$(echo "$PARENT_DATA" | jq -r '.childSatoshiNumber')

# Compare the child Satoshi number from Parent Data with the one from the source JSON
if [[ "$CHILD_SATOSHI_NUMBER_PARENT_DATA" != "$CHILD_SATOSHI_NUMBER" ]]; then
    echo "Could not verify BRC 420/69 pairing."
fi
            # Save the decrypted File Cipher to different file types based on the content
            if echo "$DECRYPTED_FILE_CIPHER" | grep -qi "PDF"; then
                echo "$DECRYPTED_FILE_CIPHER" > decrypted.pdf
                echo "Decrypted File Cipher saved as decrypted.pdf"
            elif echo "$DECRYPTED_FILE_CIPHER" | grep -qi "PNG"; then
                echo "$DECRYPTED_FILE_CIPHER" > decrypted.png
                echo "Decrypted File Cipher saved as decrypted.png"
            elif echo "$DECRYPTED_FILE_CIPHER" | grep -qi "TXT"; then
                echo "$DECRYPTED_FILE_CIPHER" > decrypted.txt
                echo "Decrypted File Cipher saved as decrypted.txt"
            elif echo "$DECRYPTED_FILE_CIPHER" | grep -qi "HTML"; then
                echo "$DECRYPTED_FILE_CIPHER" > decrypted.html
                echo "Decrypted File Cipher saved as decrypted.html"
            elif echo "$DECRYPTED_FILE_CIPHER" | grep -qi "BMP"; then
                echo "$DECRYPTED_FILE_CIPHER" > decrypted.bmp
                echo "Decrypted File Cipher saved as decrypted.bmp"
            elif echo "$DECRYPTED_FILE_CIPHER" | grep -qi "^[A-Za-z0-9+/]*={0,2}$"; then
                DECODED_BASE64=$(echo "$DECRYPTED_FILE_CIPHER" | base64 -d)
                echo "Decoded Base64:"
                echo "$DECODED_BASE64"
