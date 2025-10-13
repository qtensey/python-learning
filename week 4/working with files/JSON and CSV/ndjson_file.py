from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "media" / "file.ndjson"

with Path(FILE_DIR).open("r", encoding="utf-8", newline="") as f:
    for line in f:
        event = json.loads(line)
        print(event)