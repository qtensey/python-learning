import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "media" / "file.json"

obj = {"name": "tensey", "role": "user"}
Path(FILE_DIR).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
data = json.loads(Path(FILE_DIR).read_text(encoding="utf-8"))