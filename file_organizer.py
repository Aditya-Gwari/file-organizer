from pathlib import Path

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

for i in p.glob("*"):
    ext = i.suffix
    fld = file_types.get(ext, "others")
    dest = p  / fld
    dest.mkdir(parents = True, exist_ok = True)

