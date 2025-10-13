import os, tempfile
from pathlib import Path

def atomic_write_text(path: Path, text: str, encoding="utf-8") -> None:
    tmp_fd, tmp_name = tempfile.mkstemp(dir=str(path.parent))
    try:
        with os.fdopen(tmp_fd, "w", encoding=encoding, newline="") as tmp:
            tmp.write(text)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_name, path)   # атомарно подменяет
    finally:
        try: os.remove(tmp_name)
        except FileNotFoundError: pass

# --- пример вызова ---

# 1. Определяем путь к файлу. 
#    Path('.') означает "текущая папка".
file_path = Path('./my_document.txt')

# 2. Готовим текст, который хотим записать.
content_to_write = "Привет, мир!\nЭто безопасная, атомарная запись.\nВсе данные будут сохранены корректно."

# 3. Вызываем нашу функцию.
try:
    print(f"Попытка записать данные в файл: {file_path}")
    atomic_write_text(file_path, content_to_write)
    print("✅ Запись успешно завершена!")

    # 4. Проверяем результат: читаем файл и выводим его содержимое.
    print("\n--- Содержимое файла: ---")
    with open(file_path, "r", encoding="utf-8") as f:
        print(f.read())
    print("--------------------------")

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

finally:
    # Очистка: удаляем созданный файл после проверки
    if file_path.exists():
        os.remove(file_path)
        print(f"\nФайл {file_path} удалён для очистки.")