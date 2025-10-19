user_id_str = input("Enter user ID: ")

try:
    # Опасная операция изолирована. Ловим ТОЛЬКО ошибку от int()
    user_id = int(user_id_str)
except ValueError:
    print("Error: ID must be a number")
    exit()

database = {
    "name": "Antonio", id: 1223123,
    "name": "Frozen", id: 213144}

class NotFoundError(Exception):
    """Не удалось найти пользователя"""

# Если мы дошли сюда, значит, user_id — это точно число.
try:
    user = database.find_user(user_id)
    print(f"User name: {user.name}")
except NotFoundError:
    print("User with ID {user_id} not found.")