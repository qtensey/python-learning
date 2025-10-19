try:
    # dangerous code
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    # code to be executed in case of an error
    print("Error: you can't divide by zero!")

print("The programm continues to work")