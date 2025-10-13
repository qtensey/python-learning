import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "media" / "file.csv"

with Path(FILE_DIR).open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["id", "name"])
    w.writeheader()
    w.writerow({"id": 1, "name": "tensey"})