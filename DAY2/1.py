# OS basics

import os

# TO FIND THE CURRENT WORKING DIRECTORY
os.getcwd()
print(os.getcwd())

## TO CHANGE DIRECTORY
os.chdir("/Users/abhiraljain/Desktop/DESKTOP")
os.chdir("/Users")
print(os.getcwd())

# CREATE FOLDERS
os.mkdir("learn os")   #check folder name in explorer

# TO CREATE MULTIPLE NESTED FOLDERS
for i in range(0,100):
    os.makedirs(f"happy/day{i+1}")

#REMOVE FOLDER
os.rmdir("learn os")
for i in range(0,100):
    os.removedirs(f"happy/day{i+1}")

# LIST FILES AND FOLDERS
files = os.listdir(f"happy/day{i+1}")
print (files)

# RENAME FILES AND FOLDERS
for i in range(0,10):
    os.rename(f"happy/day{i+1}" , f"happy/progress{i+1}")

# check files exist
print(os.path.exists("learn os"))
print(os.path.exists("happy"))

# list all the files - mtlb ki count kr skte h kitne folders hai 
    
folders = os.listdir("happy")
print(folders)

for folder in folders :            ## isse pta chlta h ki folder ke andar kya hai (systematic way mai)
    print(folder)                    
    print(os.listdir(f"happy/{folder}"))


# display all the files presented
items = os.listdir()
for item in items:
    print(item)
