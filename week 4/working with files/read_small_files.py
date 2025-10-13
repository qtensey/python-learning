from pathlib import Path

# read small file
BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "media" / "file_write.txt"

text = Path(FILE_DIR).read_text(encoding="utf-8")
print(text)