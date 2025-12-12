# import os, shutil

# source = "/Users/abhiraljain/Downloads"
# dest = {
#     "images": [".jpg", ".png"],
#     "docs": [".pdf", ".docx", ".txt"],
#     "videos": [".mp4"],
#     "zips": [".zip", ".rar"]
# }

# for file in os.listdir(source):
#     name, ext = os.path.splitext(file)
    
#     for folder, exts in dest.items():
#         if ext in exts:
#             if not os.path.exists(os.path.join(source, folder)):
#                 os.mkdir(os.path.join(source, folder))

#             shutil.move(os.path.join(source, file),
#                         os.path.join(source, folder, file))
#             break


import os, shutil

source = "/Users/abhiraljain/Downloads"
dest = {
    "images": [".jpg", ".png"],
    "docs": [".pdf", ".docx", ".txt"],
    "videos": [".mp4"],
    "zips": [".zip", ".rar"]
}

for file in os.listdir(source):
    file_path = os.path.join(source, file)
    # Skip directories
    if os.path.isdir(file_path):
        continue
    name, ext = os.path.splitext(file)
    # Skip files without extension or hidden files
    if not ext or file.startswith('.'):
        continue
    for folder, exts in dest.items():
        if ext.lower() in exts:
            folder_path = os.path.join(source, folder)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            shutil.move(file_path, os.path.join(folder_path, file))
            break