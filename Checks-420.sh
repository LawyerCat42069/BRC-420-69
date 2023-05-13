#!/bin/bash

# Set the transaction ID (TXID) and the output index number
TXID="<transaction_id>"
OUTPUT_INDEX="<output_index>"

# Fetch the raw transaction
RAW_TX=$(bitcoin-cli getrawtransaction $TXID)

# Decode the raw transaction
DECODED_TX=$(bitcoin-cli decoderawtransaction $RAW_TX)

# Extract the specific output by index
OUTPUT=$(echo "$DECODED_TX" | jq ".vout[$OUTPUT_INDEX]")

# Extract the output script from the output
OUTPUT_SCRIPT=$(echo "$OUTPUT" | jq -r '.scriptPubKey.hex')

# Decode the script and check for inscribed data
INSRIPTION=$(echo "$OUTPUT_SCRIPT" | xxd -r -p | awk '/OP_RETURN/ { print $2 }' | xxd -r -p)

# Verify if the inscribed data is JSON
if [[ $(echo "$INSRIPTION" | jq -e . >/dev/null 2>&1; echo $?) -eq 0 ]]; then
    echo "Inscribed JSON data found:"
    echo "$INSRIPTION"
else
    echo "No inscribed JSON data found."
fi
