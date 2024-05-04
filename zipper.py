import os
import zipfile

# List of folder paths you want to zip
folders_to_zip = ['./data', './figures', './analysis', './narrative']

# Path for the output zip file
output_zip_file = '3039557445_3039556483_3039559460.zip'

# Create a new zip file
with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add folders
    for folder in folders_to_zip:
        for root, dirs, files in os.walk(folder):
            for file in files:
                zip_path = os.path.join(root, file)
                zipf.write(zip_path, arcname=zip_path)

print(f'Created zip file: {output_zip_file}')
