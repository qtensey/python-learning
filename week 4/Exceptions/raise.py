def set_age(age):
    if age < 0:
        # Если возраст отрицательный, это ненормально.
        # Вызываем исключение, чтобы сообщить об этом.
        raise ValueError("age cannot be negative!")
    print(f"age set: {age}")

try:
    set_age(25)
    set_age(-10)
except ValueError as e:
    print(f"error validated data: {e}") # age cannot be negative!