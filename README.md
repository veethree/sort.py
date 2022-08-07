# sort.py
A little script that sorts files into sub-folders based on their extensions.
It can be set up to group filetypes together into categories (It does this by default) or just each file type into its own folder. This can be set up with the settings.py file. The settings.py file also contains a list called "exclude". Any file types found there will be ignored by the sorter. By default it only ignores file types for shortcuts (in windows).

If you call the script without an argument, It will sort the folder the script is in, Otherwise it will sort the folder provided.

Usage
```
python sort.py "C:\Users\yourmom\Downloads"
```

This script becomes more useful if you fuck around with the windows registry a bit to be able to run it from a context menu.
