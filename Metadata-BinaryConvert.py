import os
from bson import BSON

os.chdir('C:\\SET\\DIRECTORY')
 
# Your original metadata
metadata_dict = {
   "Token Designation": "BRC-69",
   "Satoshi Number": "XXXXXXXXXXXXXXXX",
   "Parent Satoshi Number": "UNKNOWN - PROVENANCE QUESTIONABLE",
   "Collection Name": "Name",
   "Collection Size": "XXXX",
   "Collection Number": "XXXX of XXXX",
   "Background": "Black",
   "Trait Category": "Trait Name",

}

#repeat traits as needed


# Convert the metadata to BSON
bson_data = BSON.encode(metadata_dict) 

dir_path = r'C:\\DESIRED\\FILEPATH'
os.makedirs(dir_path, exist_ok=True)  # creates the directory if it doesn't exist

try:
    with open(os.path.join(cwd, 'FILENAME.bson'), 'wb') as f:
