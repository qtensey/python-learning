# asda

"""This i
s t
he main mo
dule of th
e applic
ation.
"""

x = 5
name = "Andrij"
is_admin = True


if x > 0:
    print(f"Hello, {name}!")
elif x == 0:
    print("Goodbye!")
else:
    print("Negative number")


while x > 0:
    print(x)
    x -= 1


def say_hello(name):
    return f"Hello, {name}!"


class User:
    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = is_admin

    def greet(self):
        return f"Welcome, {self.name}!"
    

int, float, str, bool, list, dict, tuple, set


list = [1, 2, 3, 4, 5]
dict = {"name": "Andrij", "age": 30}
tuple = (1, 2, 3)
set = {1, 2, 3, 4, 5}