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
def sort_folder():

    path_str = input("Enter the path to the file folder : ")

    path = Path(path_str)

    if not path.is_dir():
        print("Wrong path!!")
        return
    
    for i in path.glob("*"):

        if not i.is_dir():
            ext = i.suffix

            fld = file_types.get(ext.lower() , "others")
            dest = path  / fld
            dest.mkdir(parents = True, exist_ok = True)

            shutil.move(i, dest)
    print("All files in the folder have been sorted...")

def sort_file():

    path_str = input("Enter the path to the file : ")

    path = Path(path_str)

    if not path.exists():
        print("Wrong path!!")
        return

    ext = path.suffix
    fld = file_types.get(ext.lower() , "others")

    folder = path.parent

    dest = folder / fld

    dest.mkdir(parents = True, exist_ok = True)
    try:
        shutil.move(path, dest)
        print("The file has been sorted...")
    except shutil.Error as e:
        print("The file already exists in your target folder...")

        n = input("Would you like to REPLACE (1) it or RENAME (2) it? : ")
        if n == "1":
            path.replace(dest / path.name)
            print("File Replaced!")

        elif n == "2":
            new_path = path.parent / f"{path.stem}(1){path.suffix}"
            path.rename(new_path)
            
            
            print("File Renamed and Sorted!!")

sort_file()
