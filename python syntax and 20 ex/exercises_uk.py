# Python Тиждень 1 - Маленькі вправи
# ==================================

# 🔹 Базові змінні та операції

# 1. Виведи рядок "Hello, World!".
print("Hello, World!")

# 2. Запитай у користувача два числа і виведи їх суму.
x, y = input("Enter two numbers separated by space: ").split()
print(f'The sum is: {int(x) + int(y)}')

# 3. Обчисли вираз (17 * 3) + (22 / 2) і виведи результат.
result = (17 * 3) + (22 / 2)
print(f'The result of the expression is: {result}')

# 4. Запитай число і перевір, чи є воно парним або непарним.
doubles = int(input("Enter a number to check if it is a pair or not: "))
if doubles % 2 == 0:
    print(f'The numper {doubles} is a pair')
else:
    print(f'the number {doubles} is not a pair')

# 5. Запитай три числа і виведи найбільше з них.
x, y, z = input("Enter three numbers separated by space to find the biggest:").split()
biggest = max(int(x), int(y), int(z))
print(f'The biggest number is: {biggest}')

# 🔹 Рядки
# 6. Запитай рядок у користувача і виведи його довжину.
print(f'String lenth: {len(input("Enter a string to check is length: "))}')

# 7. Переверни рядок "python" → "nohtyp".
print('Reversed string "python": ' + 'python'[::-1])

# 8. Порахуйте, скільки разів літера "a" зустрічається в рядку.
string = input("Enter a string to count how many times the letter 'a' occurs: ")
count_a = string.lower().count('a')
print(f'The letter "a" occurs {count_a} times in the string.')

# 9. Перевір, чи є введений рядок паліндромом.
palindrom = input("Enter a string to check if it is a palindrom: ")
if palindrom == palindrom[::-1]:
    print(f'The string "{palindrom}" is a palindrom')
else:
    print(f'The string "{palindrom}" is not a palindrom')

# 10. Запитай ім’я та вік, виведи: "Мене звати ІМ'Я, мені X років".
name, age = input("Enter your name and age separated by space: ").split()
print(f'My name is {name}, I am {age} years old.')


# 🔹 Списки
# 11. Знайди суму елементів списку [1, 2, 3, 4, 5].
numbers = [1, 2, 3, 4, 5]
print(f'Sum og the list elements: {sum(numbers)}')

# 12. Знайди середнє арифметичне списку [10, 20, 30, 40].
average = sum([10, 20, 30, 40]) / len([10, 20, 30, 40])
print(f'The average of the list is: {average}')

# 13. Знайди мінімальне і максимальне число у списку.
numbers = [5, 3, 8, 1, 4]
min_num = min(numbers)
max_num = max(numbers)
print(f'Minimum number in the list is: {min_num}, maximum number in the list is: {max_num}')

# 14. Із масиву [1, 1, 2, 3, 3, 4] створи список тільки з унікальних елементів.
unique_numbers = list(set([1, 1, 2, 3, 3, 4]))
print(f'List with unique elements: {unique_numbers}')

# 15. Дано список чисел, виведи перші 3 і останні 2 елементи.
numbers = [10, 20, 30, 40, 50, 60, 70]
print(f'First 3 elements: {numbers[:3]}, last 2 elements: {numbers[-2:]}')


# 🔹 Словники

# 16. Створи словник з ключами "name", "age", "city" і задай значення.
person = {
    "name": "Andrij",
    "age": 30,
    "city": "Kyiv"
}
print(f'Person dictionary: {person}')

# 17. Виведи значення за ключем "name".
print(f'Name from the dictionary: {person["name"]}')

# 18. Дано текст, порахуй, скільки разів зустрічається кожне слово (використай словник).
text = "this is a sample text this text is for counting words"
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f'Word count: {word_count}')

# 19. Створи словник: {"fruits": ["apple", "banana"], "numbers": [1, 2, 3]}, виведи другий фрукт.
my_dict = {
    "fruits": ["apple", "banana"],
    "numbers": [1, 2, 3]
}
print(f'Second fruit in the list: {my_dict["fruits"][1]}')

# 20. Введи рядок і створи словник: ключ — символ, значення — скільки разів він зустрічається.
input_string = input("Enter a string to create a dictionary with character counts: ")
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f'Character count dictionary: {char_count}')