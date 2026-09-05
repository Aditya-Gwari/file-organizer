from pathlib import Path
import shutil

file_types = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    # Images
    ".jpg": "Photos",
    ".jpeg": "Photos",
    ".png": "Photos",
    ".gif": "Photos",

    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",

    # Audio
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music"
}

s = input("Enter the file path : ")

p = Path(s)

print(p)

exts = []

for i in p.glob("*"):

    if not i.is_dir():
                ext = i.suffix
                if ext not in exts:
                    exts.append(ext)

    ext = i.suffix
    fld = file_types.get(ext, "others")
    dest = p  / fld
    dest.mkdir(parents = True, exist_ok = True)

for i in exts:
    print(i)
    m = file_types.get(i, "others")
    for l in p.glob("*"+i):
        shutil.move(l, p / m)
