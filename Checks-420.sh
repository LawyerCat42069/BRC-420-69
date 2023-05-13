#!/bin/bash

# Read the data from the source file
SOURCE_FILE="source.json"
PARENT_SATOSHI_NUMBER=$(jq -r '.parentSatoshiNumber' "$SOURCE_FILE")
FILE_CIPHER=$(jq -r '.fileCipher' "$SOURCE_FILE")
METADATA_CIPHER=$(jq -r '.metadataCipher' "$SOURCE_FILE")

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
