from pathlib import Path

# exclusive file write
BASE_DIR = Path(__file__).resolve().parent    # the folder where thw current .py file is located
FILE_DIR = BASE_DIR / "file_write_exclusive.txt"

with open(FILE_DIR, "x", encoding="utf-8") as f:    # x - create only if not created
    f.write("{}")