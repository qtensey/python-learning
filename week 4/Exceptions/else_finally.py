# block else:
# Код в блоке else выполняется только в том случае, если в блоке try не произошло никаких исключений.
try:
    # dangerous operation
    file = open("my_data.txt", "r")
except FileNotFoundError:
    print("file is note found")
else:
    # 2. Этот код выполнится, только если файл успешно открылся
    print("File opened successfully. Reading data...")
    data = file.read()
    file.close
    print(data)

#block finally
# Для действий, которые нужно выполнить гарантированно. Например, закрыть файл, разорвать соединение с базой данных или очистить временные ресурсы.
file = None

try:
    file = open("important_file.txt", "r")
    # work with file ...
except FileNotFoundError:
    print("file is not found")
finally:
    # Этот код выполнится в любом случае
    if file:
        print("close the file")
        file.close()