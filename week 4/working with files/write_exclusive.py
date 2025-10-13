from pathlib import Path

# exclusive file write (do not overwrite someone else's)
BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "media" / "file_write_exclusive.txt"

with open(FILE_DIR, "x", encoding="utf-8") as f:    # x - create only if not created
    f.write("{}")