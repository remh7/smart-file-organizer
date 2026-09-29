from pathlib import Path
import shutil
downloads = Path('Downloads')


categories = {
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
}


def get_unique_path(folder,filename):
    destination = folder / filename 

    if not destination.exists():
       return destination

    counter = 1

    while True:
       new_name = f"{destination.stem}_{counter}_{destination.suffix}"
       new_destination = folder / new_name
       if not new_destination.exists():
              return new_destination

       counter += 1


report = {}
for file in downloads.iterdir():
    if not file.is_file():
     continue

    category = categories.get(file.suffix.lower(), "Others")
    report[category] = report.get(category, 0) + 1

    folder = downloads / category

    folder.mkdir(exist_ok=True)

    destination = get_unique_path(folder, file.name)
    shutil.move(file,destination)

    print(f"{file.name} -> {category}")

print("\n--- Report ---")

for category, count in report.items():
    print(f"{category}: {count} files")
