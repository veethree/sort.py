# sort.py
A little script that sorts files into sub-folders based on their extensions.
It can be set up to group filetypes together into categories (It does this by default) or just each file type into its own folder. This can be set up with the settings.py file. The settings.py file also contains a list called "exclude". Any file types found there will be ignored by the sorter. By default it only ignores file types for shortcuts (in windows).

If you call the script without an argument, It will sort the folder the script is in, Otherwise it will sort the folder provided.

Something to keep in mind, At the moment it doesn't really worry about overwriting files and such. But if it attempts to overwrite a file, It just silently crashes.

Usage
```
python sort.py "C:\Users\yourmom\Downloads"
```

This script becomes more useful if you fuck around with the windows registry a bit to be able to run it from a context menu.
![screenshot](https://github.com/veethree/sort.py/blob/main/sort.png)


Here's my disgusting downlods folder
![screenshot](https://github.com/veethree/sort.py/blob/main/before.png)

And here its sorted. Beautiful.
![screenshot](https://github.com/veethree/sort.py/blob/main/after.png)
