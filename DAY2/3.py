## File Operations with shutil (Important for Automation)

import shutil

# copy files
shutil.copy("data.txt", "backup/data.txt")

# copy folder
shutil.copytree("happy", "destination")

# rename files
shutil.move("1.txt" , "rename.txt")

# delete folders.  -- this is permanent deletion.
shutil.rmtree("backup")


## Creating ZIP & Archive Files
shutil.make_archive("backup", "zip", "learn os")



## modern and cleaner approachv -- Pathlib

from pathlib import Path

# basic usage 
path = Path("happy")
print(path.exists())
print(path.is_dir())

# create files and folders
for file in Path(".").glob("*.txt"):
    print(file.name)

# iterate files
for file in Path(".").glob("*.txt"):
    print(file.name)



