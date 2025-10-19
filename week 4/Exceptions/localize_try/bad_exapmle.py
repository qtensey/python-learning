database = "Заглушка"

try:
    user_id_str = input("Enter ID user: ")
    user_id = int(user_id_str)
    user = database.find_user(user_id)
    print(f"User name: {user.name}")
except ValueError:
    # Мы поймали ValueError, но откуда он пришёл?
    # От int()? Или, может, функция find_user() тоже может его вызвать? Мы не знаем.
    print("Error: ID must be a number.")