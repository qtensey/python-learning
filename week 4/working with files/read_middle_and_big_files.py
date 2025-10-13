from pathlib import Path

# read middle file
BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "media" / "file_write.txt"

with Path(FILE_DIR).open("r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())