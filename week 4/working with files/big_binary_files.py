from pathlib import Path

# copy big binary file (video)
BASE_DIR = Path(__file__).resolve().parent    # the folder where thw current .py file is located
FILE_DIR = BASE_DIR / "media" / "movie.mp4"
COPY_FILE = BASE_DIR / "media" / "copy.mp4"

with open(FILE_DIR, "rb") as f_original, open(COPY_FILE, "wb") as f_copy:    # "rb" - read binary
    while chunk := f_original.read(1024 * 1024):
        f_copy.write(chunk)