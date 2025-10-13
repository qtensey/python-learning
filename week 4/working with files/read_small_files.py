from pathlib import Path

# read small file
text = Path("file.txt").read_text(encoding="utf-8")
print(text.strip())