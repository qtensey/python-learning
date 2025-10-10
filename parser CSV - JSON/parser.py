import csv
import json


csv_file = 'input.csv'
json_file = 'output.json'


with open(csv_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)


with open(json_file, mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


print("Готово! Файл збережений як", json_file)