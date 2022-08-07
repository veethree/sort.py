# This dictionary tells the sorter into what folder a file type should go
category = {
    # ACRHIVE
    "zip":"Archive",
    "rar":"Archive",
    "7z":"Archive",
    "tar.gz":"Archive",

    "mp3":"Audio",
    "wave":"Audio",
    "wav":"Audio",
    "ogg":"Audio",
    "FLAC":"Audio",

    # IMAGE
    "jpg":"Image",
    "jpeg":"Image",
    "png":"Image",
    "tif":"Image",
    "tiff":"Image",
    "bmp":"Image",
    "gif":"Image",
    "raw":"Image",
    "cr2":"Image",
    "nef":"Image",
    "orf":"Image",
    "sr2":"Image",

    # VIDEO
    "mp4":"Video",
    "avi":"Video",
    "mov":"Video",
    "flv":"Video",
    "mkv":"Video",
    "wmv":"Video",
    "svf":"Video",
    "webm":"Video",
    "avchd":"Video",

    # DOCUMENT
    "xlsx":"Document",
    "pdf":"Document",
    "txt":"Document",
    "doc":"Document",
    "docx":"Document",
    "html":"Document",
    "htm":"Document",
    "odt":"Document",
    "xls":"Document",
    "ppt":"Document",
    "pptx":"Document",
}

# File types in this list will be excluded from sorting
exclude = [
    "lnk", "url", "cda"
]