from pathlib import Path
import shutil
downloads = Path('Downloads')

categories = {
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
}
report = {}
for file in downloads.iterdir():
    if not file.is_file():
     continue

    category = categories.get(file.suffix.lower(), "Others")
    report[category] = report.get(category, 0) + 1

    folder = downloads / category

    folder.mkdir(exist_ok=True)

    shutil.move(file,folder / file.name)

    print(f"{file.name} -> {category}")

print("\n--- Report ---")

for category, count in report.items():
    print(f"{category}: {count} files")
