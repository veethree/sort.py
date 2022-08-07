# sort.py: A little script that sorts files in a folder, Either by file type or by date
# Can be called with the following arguments
# 'python sort.py [Path to folder] [Mode (type/date)]

# The 'type' mode will sort the files into subfolders based on the filetype. Categories can be set up in the settings.py file.
# File types without a category will be placed in a folder named after the extension.
# Examples:
# C://Users/yourmom/Downloads/file.mp3 => C:/Users/yourmom/Downloads/Audio/file.mp3
# C://Users/yourmom/Downloads/file.js => C:/Users/yourmom/Downloads/js/file.js
#

# The 'date' mode will sort the files into subfolders based on the date of creation.
# Examples:
# C://Users/yourmom/Downloads/file.mp3 => C:/Users/yourmom/Downloads/2022/03 March/13 - file.mp3
from os import listdir, mkdir, rename
from os.path import isfile, isdir, basename, dirname, realpath, getsize, getctime, join, splitext
from sys import argv
from datetime import datetime
from tkinter import messagebox
from tkinter.tix import DirSelectBox
from settings import category, exclude, allow_rename
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

# Working directory, Either the first argument, Or the path of the script
directory = dirname(realpath(__file__))
mode = "type"
if len(argv) > 1:
    if isdir(argv[1]):
        directory = argv[1]
    else:
        print(f"'{argv[1]}' is not a valid directory!")
    
    if len(argv) > 2:
        if argv[2] == "type" or argv[2] == "date":
            mode = argv[2]

# Gathering the files and all relevant data into a neat list
files = []
size = 0
count = 0
for item in listdir(directory):
    if isfile(f"{directory}\{item}"):
        if item != basename(__file__):
            # Date stuff
            day, month, year = datetime.fromtimestamp(getctime(join(directory, item))).strftime("%d-%m %B-%Y").split("-")

            # Type stuff
            filename, filetype = splitext(item)
            filetype = filetype.strip(".")

            if not filetype in exclude:
                files.append({
                    "path":join(directory, item),
                    "name":item,
                    "name_stripped":filename,
                    "type":filetype,
                    "cday":day,
                    "cmonth":month.strip("0"),
                    "cyear":year
                })
                count += 1
                size += getsize(f"{directory}\{item}")

def sort_by_date():
    for file in files:
        # Creating YEAR directory if it doesn't exist
        if not isdir(join(directory, file["cyear"])):
            mkdir(join(directory, file["cyear"]))
        # Creating MONTH directory if it doesn't exist
        if not isdir(join(directory, file["cyear"], file["cmonth"])):
            mkdir(join(directory, file["cyear"], file["cmonth"]))

        # Moving files to their folders
        destination = join(directory, file["cyear"], file["cmonth"], {file["name"]})
        if allow_rename:
            destination = join(directory, file["cyear"], file["cmonth"], f'{file["cday"]} - {file["name"]}')

        rename(join(directory, file["path"]), destination)

def sort_by_type():
    for file in files:
        destination_folder = ""
        # Creating category folders
        if file["type"] in category:
            if not isdir(join(directory, category[file["type"]])):
                mkdir(join(directory, category[file["type"]]))
            destination_folder = join(directory, category[file["type"]])

        else:
            # Creating filetype folder if one doesnt exist
            #if not isdir(f'{directory}\{file["type"]}'):
            if not isdir(join(directory, file["type"])):
                mkdir(join(directory, file["type"]))
            destination_folder = join(directory, file["type"])
 
        
        # Moving file to the appropraite folder
        rename(join(directory, file["path"]), join(destination_folder, file["name"]))

# Checking in with the user if he really wants to do this, In case he fucks around and tries to sort system32 or something.
def confirm():
    go = messagebox.askyesno("Warning", f"You are about to sort (by {mode}) {count} files ({convert_size(size)}) in the following directory\n'{directory}'\nAre you sure?")
    if go:
        if mode == "date":
            sort_by_date()
        elif mode == "type":
            sort_by_type()

confirm()