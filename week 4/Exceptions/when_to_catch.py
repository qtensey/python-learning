# Когда СЛЕДУЕТ перехватывать исключения
# Перехватывать нужно ожидаемые, штатные ошибки, для которых у тебя есть "план Б".

# 1 - Валидация пользовательского ввода:
# Ситуация: Программа просит ввести возраст, а пользователь вводит текст.
# Исключение: ValueError.
# Что делать? Сообщить пользователю: "Нужно ввести число, попробуйте ещё раз".
while True:
    try:
        age = int(input("enter your age: "))
        break
    except ValueError:
        print("Error: age must be a number. Please re-enter.")

# 2 - Работа с внешними ресурсами (файлы, сеть)
# Ситуация: Вы пытаетесь прочитать файл конфигурации.
# Исключение: FileNotFoundError.
# Что делать? Создать этот файл с настройками по умолчанию или сообщить пользователю, что файл не найден и программа не может работать.
import json

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Configuration file not found. Creating a new one...")

# 3 - Повторные попытки при временных сбоях
# Ситуация: Вы получаете данные по API.
# Исключение: Timeout или ConnectionError.
# Что делать? Подождать секунду и попробовать снова несколько раз.
import requests
import time

for i in range(3):
    try:
        response = requests.get("https://api.example.com/data")
        response.raice_for_status()
        break
    except requests.exceptions.RequestException as e:
        print(f"Attempt {i+1} failed: {e}. Repeat int 2 seconds...")
        time.sleep(2)


# Когда НЕ СЛЕДУЕТ перехватывать исключения
# Не нужно перехватывать неожиданные ошибки, которые свидетельствуют о багах в коде или о критическом состоянии, из которого программа не может восстановиться.

# Ошибки программиста (баги)
# NameError: Вы использовали переменную, которую не создали.
# TypeError: Вы пытаетесь сложить число и строку (5 + "яблоко").
# IndexError: Вы обращаетесь к элементу списка по несуществующему индексу.
try:
    # 100 lines of code ...
    result = some_list[non_existent_index] # IndexError
    # 100 lines of code ...
except Exception:
    print("Что-то пошло не так, но мы продолжаем!")