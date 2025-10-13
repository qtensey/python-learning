from pathlib import Path

with open("file.txt", 'r', encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# read small file
text = Path("file.txt").read_text(encoding="utf-8")
print(text)

# read midle file
with Path("file.txt").open("r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Копирование большого файла в другой файл
src = Path("movie.mp4")
dst = Path("copy.mp4")

with src.open("rb") as f_src, dst.open("wb") as f_dst:
    while chunk := f_src.read(1024 * 1024):
        f_dst.write(chunk)

# ------- write -------

# normal
Path("file_writing.txt").write_text("This is new string\n", encoding="utf-8")

# exclusive
with open("file_writing_2.txt", "x", encoding="utf-8") as f:
    f.write("{}")

# atomic
...

# ------ JSON, CSV, NDJSON ------

# JSON:
import json

obj = {"name": "tensey", "role": "user"}
Path("user.json").write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
data = json.loads(Path("user.json").read_text(encoding="utf-8"))