# import os,shutil

# base_folder= os.getcwd() + "\\data"
# files = os.listdir(base_folder)
# # files =base_folder.iterdir()
# # print(files)
# for file in  files:
#     exten = file.split(".")[-1] if file in '.' else 'unknown'
#     if os.path.isfile(file):
#         taken = os.path.join(base_folder,file)
#         put_on = os.path.join(base_folder,exten)
#         if not os.path.exists(put_on):
#             os.makedirs(put_on)
#         shutil.move(taken,put_on)


import os
import shutil
from pathlib import Path

# Define the folder to organize
base_folder = Path.cwd() / 'data'
print(f"Organizing folder: {base_folder}")

# Make sure the folder exists
if not base_folder.exists():
    print("The folder does not exist.")
    exit()

# Loop through all items in the folder
for item in base_folder.iterdir():
    if item.is_file():
        # Get the file extension (or 'unknown' if no extension)
        ext = item.suffix[1:].lower() if item.suffix else 'unknown'

        # Create the destination folder path
        dest_folder = base_folder / ext
        dest_folder.mkdir(exist_ok=True)

        # Move the file
        shutil.move(str(item), str(dest_folder / item.name))
