from pathlib import Path

# normal file write
BASE_DIR = Path(__file__).resolve().parent    # the folder where thw current .py file is located
FILE_DIR = BASE_DIR / "file_write.txt"

Path(FILE_DIR).write_text("Hello\n", encoding="utf-8")