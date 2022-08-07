# A file sorting script that sorts files into subfolders based on their extension.

from os import listdir, mkdir, rename
from os.path import isfile, splitext, isdir, basename, dirname, realpath, getsize
from sys import argv
import math
from tkinter import messagebox
from settings import category, exclude

# Source: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

# The directory to be sorter, Either the directory of the script,
# Or one provided as an argument
directory = dirname(realpath(__file__))
if len(argv) > 1:
    if isdir(argv[1]):
        directory = argv[1]
    else:
        print(f"'{argv[1]}' is not a valid directory!")

# Creating a list of files to be sorted
# Also counting them, And adding up their sizes while we're at it.
files = []
size = 0
file_count = 0
for item in listdir(directory):
    if isfile(f"{directory}\{item}"):
        if item != basename(__file__):
            filename, filetype = splitext(item)
            filetype = filetype.strip(".")
            if not filetype in exclude:
                files.append({"filename":filename, "filetype":filetype})
                file_count += 1
                size += getsize(f"{directory}\{item}")

# Doing all the sorting business.
def sort():
    for file in files:
        destination_folder = ""
        # Creating category folders
        if file["filetype"] in category:
            if not isdir(f'{directory}\{category[file["filetype"]]}'):
                mkdir(f'{directory}\{category[file["filetype"]]}')
            destination_folder = f'{directory}\{category[file["filetype"]]}'
        else:
            # Creating filetype folder if one doesnt exist
            if not isdir(f'{directory}\{file["filetype"]}'):
                mkdir(f'{directory}\{file["filetype"]}')
            destination_folder = f'{directory}\{file["filetype"]}'
        
        # Moving file to the appropraite folder
        rename(f'{directory}\{file["filename"]}.{file["filetype"]}', f'{destination_folder}\{file["filename"]}.{file["filetype"]}')

# Checking in with the user if he really wants to do this, In case he fucks around and tries to sort system32 or something.
def confirm():
    go = messagebox.askyesno("Warning", f"You are about to sort {file_count} files ({convert_size(size)}) in the following directory\n'{directory}'\nAre you sure?")
    if go:
        sort()

confirm()