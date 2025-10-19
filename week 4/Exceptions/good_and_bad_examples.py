# bad:
try:
    print("Hello world!")
except Exception: # Catches absolutely everything!
    print("Some error occured")

# good:
try:
    user_input = input("Enter number:")
    number = int(user_input)
    print(f"The square of your number: {number ** 2}")
except ValueError:
    print("Error: You entered an invalid number!")
except KeyboardInterrupt: # Ctrl + C
    print("\nyou have cancelled your imput")