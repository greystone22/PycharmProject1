# greystone22
# 05/27/2023 14:44

import os

# Path to the Documents folder
documents_folder = os.path.expanduser(r"Path to documents folder")

# List all files in the Documents folder
file_list = []
for root, dirs, files in os.walk(documents_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)

# Print the list of installed files
for file_path in file_list:
    print(file_path)
