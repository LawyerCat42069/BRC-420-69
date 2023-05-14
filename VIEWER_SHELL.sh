#!/bin/bash

extracted_file_path="/path/to/extracted/file.html"

# Check if the extracted file exists
if [ ! -f "$extracted_file_path" ]; then
    echo "File not found: $extracted_file_path"
    exit 1
fi

# Open a subshell with restricted privileges
(
    # Disable potentially dangerous commands
    alias rm="echo 'rm command is disabled'"
    alias mv="echo 'mv command is disabled'"
    alias cp="echo 'cp command is disabled'"
    alias mkdir="echo 'mkdir command is disabled'"
    alias rmdir="echo 'rmdir command is disabled'"

    # Set necessary environment variables for the shell
    export PAGER="less"
    export BROWSER="your-preferred-browser"
    
    # Change directory to a safe location if needed
    cd /path/to/safe/location
    
    #place for API calls to the Bitcoin Blockchain 
    
    # Run the default shell for viewing the extracted contents
    $SHELL
)
