# Smart File Organizer 📁

A simple Python script that automatically organizes files in the `Downloads` folder based on their file extensions.

## Features

* Organizes files into categories such as:

  * Music
  * Videos
  * Images
  * Documents
  * Archives
  * Others
* Automatically creates category folders.
* Supports uppercase and lowercase file extensions.

## Requirements

* Python 3.x

## Usage

1. Put the files you want to organize inside the `Downloads` folder.
2. Run the script:

```bash
python main.py
```

3. Files will be moved into their corresponding folders automatically.

## Project Structure

```text
smart-file-organizer/
├── main.py
├── README.md
└── .gitignore
```

## Example

Before:

```text
Downloads/
├── song.mp3
├── photo.jpg
├── movie.mp4
└── document.pdf
```

After:

```text
Downloads/
├── Music/
│   └── song.mp3
├── Images/
│   └── photo.jpg
├── Videos/
│   └── movie.mp4
└── Documents/
    └── document.pdf
```

## License

This project is for learning and personal use.

## 👨‍💻 Developer

Developed and maintained by **remh7**