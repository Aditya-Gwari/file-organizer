# File Organizer 📁

A simple Python program that automatically organizes files into folders based on their file extensions.

## 📌 What It Does

The program asks for the path of a folder containing different types of files.

For example:

    files/
    ├── photo.jpg
    ├── assignment.pdf
    ├── song.mp3
    ├── notes.txt
    └── movie.mp4

The program automatically creates appropriate folders and moves the files into them:

    files/
    ├── Photos/
    │   └── photo.jpg
    ├── Documents/
    │   ├── assignment.pdf
    │   └── notes.txt
    ├── Music/
    │   └── song.mp3
    └── Videos/
        └── movie.mp4

## ✨ Features

- Takes the folder path from the user
- Automatically detects file extensions
- Creates category folders automatically
- Moves files into their appropriate categories
- Supports multiple extensions for each category
- Places unsupported file types into an `others` folder
- Ignores directories while detecting file extensions

## 📂 Supported File Types

| Category | Extensions |
|----------|------------|
| Documents | `.pdf`, `.doc`, `.docx`, `.txt` |
| Photos | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Videos | `.mp4`, `.mov`, `.avi` |
| Music | `.mp3`, `.wav`, `.flac` |
| Others | Unsupported file extensions |

More file extensions can be added by modifying the `file_types` dictionary.

## 🛠️ Technologies Used

- Python
- `pathlib`
- `shutil`

## 🧠 Python Concepts Practiced

This project helped me practice:

- Dictionaries
- Lists
- `for` loops
- `if` statements
- User input
- Dictionary `.get()`
- `pathlib.Path`
- `Path.glob()`
- `Path.suffix`
- `Path.is_dir()`
- `Path.mkdir()`
- `shutil.move()`

## 🚀 How to Use

### 1. Clone the repository

    git clone https://github.com/Aditya-Gwari/file-organizer.git

### 2. Open the project directory

    cd file-organizer

### 3. Run the program

    python organizer.py

### 4. Enter the folder path

The program will ask:

    Enter the file path:

Enter the path of the folder you want to organize.

Example:

    C:\Users\Aditya\Desktop\files

The program will then create the required category folders and move the files automatically.

## ⚠️ Important

This program **moves** files rather than copying them.

It is recommended to test the program on a folder containing test files before using it on important data.

Make sure the folder path entered is correct before running the program.

## 🔮 Future Improvements

- [ ] Add more file extensions
- [ ] Handle uppercase extensions such as `.JPG`
- [ ] Improve handling of files without extensions
- [ ] Add duplicate-file handling
- [ ] Add a dry-run mode
- [ ] Add logging
- [ ] Add command-line arguments
- [ ] Allow custom categories
- [ ] Add an undo feature
- [ ] Improve error handling
- [ ] Add automated tests
- [ ] Add a graphical user interface

## 📈 Project Status

**Version 1.0**

The first version of the File Organizer is complete.

The current version focuses on basic file organization and practicing Python filesystem operations. Future versions will gradually add more features and improvements.

## 👤 Author

**Aditya Gwari**

Built as a Python learning project.
