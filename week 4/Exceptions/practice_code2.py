import time
from typing import Final
from pathlib import Path


class LoadError(Exception):
    """Ошибка загрузки файла (обертка над FileNotFoundError)."""


class BadInput(Exception):
    """Плохой ввод (обертка над ValueError при конверсии в int)."""


def read_number(path: str) -> int:
    """
    Читает целое число из файла `path`.

    Поведение:
    - FileNotFoundError -> LoadError("файл не найден")
    - ValueError при int() -> BadInput("ожидалось целое")
    - PermissionError -> до 3 попыток чтения с паузами, затем проброс исключения
    - Все прочие исключения не перехватываются и пробрасываются дальше
    """
    attempts: Final[int] = 3

    for i in range(1, attempts + 1):
        try:
            # with гарантирует закрытие файла в любых случаях, если он открылся
            with open(path, "r", encoding="utf-8") as f:
                raw = f.read().strip()

            try:
                return int(raw)
            except ValueError as e:
                # Оборачиваем только ошибку конверсии
                raise BadInput("ожидалось целое") from e

        except PermissionError as e:
            # Ретрай только на PermissionError
            if i < attempts:
                # Небольшой экспоненциальный бэкофф
                time.sleep(0.1 * (2 ** (i - 1)))
                continue
            # После 3-й попытки — сдаёмся и пробрасываем PermissionError
            raise

        except FileNotFoundError as e:
            # Оборачиваем отсутствие файла
            raise LoadError("файл не найден") from e


BASE_DIR = Path(__file__).resolve().parent    # the folder where the current .py file is located
FILE_DIR = BASE_DIR / "files" / "text.txt"

read_number(FILE_DIR)