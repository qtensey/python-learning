from pathlib import Path
import time

def read_number(path: str) -> int:
    """
    Читает целое число из файла.
    Повторяет попытку 3 раза при ошибке доступа (PermissionError).
    """

    max_attempts = 3

    for attempt in range(max_attempts):
        try:
            with open(path, 'r') as f:
                content = f.read()

            number = int(content.strip())
            print(number)
            return number
        except FileNotFoundError:
            raise Exception("LoadError: файл не найден")
        except ValueError:
            raise("BadInput: ожидалось целое")
        except PermissionError as e:
            # Ошибка 3: Нет доступа. Это временная проблема.
            print(f"Попытка {attempt + 1}/{max_attempts}: Ошибка доступа...")

            if attempt == max_attempts - 1:
                print("Не удалось получить доступ к файлу после 3 попыток.")
                raise e
            time.sleep(0.1)
    raise Exception("Не удалось прочитать файл по неизвестной причине.")


BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "files" / "text.txt"

read_number(FILE_DIR)