# sort.py
A little script that sorts files in a folder. It has two sort modes, By type, And by date created.

Usage:
```
python sort.py [path to folder] [mode (type or date)]

python sort.py "C:\Users\Your Mother\Downloads" type
```

## Type mode
In type mode, The files will be sorted by their extensions. File extensions can be grouped together into categories in the settings.py file. By default it
sorts some common Archives (zip, rar, etc), Images (png, jpg, etc.), Audio (mp3, wav, etc.) and Documents (doc, xlsx, etc) into categories.

## Date mode
In date mode, The files will be sorted by their creation date. First by year, Then by month. Then the day of the month the file was created is added to the filenames (If "allow_rename" is set to True in settings.py)

## Settings.py
In the settings.py you get a little control over the sorting. It contains a dictionary with the following format that can be used to create categories

```
category = {
  "[Extension]":"[Category]"
}
```

So if you want all archive files to be grouped together you'd do something like
```
category = {
  "zip":"Archive",
  "7z":"Archive",
  "rar":"Archive"
  etc...
}
```
The default settings.py already does this.

There is also a list called "exclude". Any extensions in that list will be ignored. By default it ignores a couple windows shortcut files.

Then there is a boolean called "allow_rename" If its set to true, The script will be allowed to rename files in date mode.


This script becomes more useful if you fuck around with the windows registry a bit to be able to run it from a context menu.

![screenshot](https://github.com/veethree/sort.py/blob/main/sort.png)


Here's my disgusting downlods folder
![screenshot](https://github.com/veethree/sort.py/blob/main/before.png)

And here its sorted. Beautiful.
![screenshot](https://github.com/veethree/sort.py/blob/main/after.png)
