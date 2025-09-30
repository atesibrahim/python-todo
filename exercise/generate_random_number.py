import random

number1 = int(input("Enter the lower bound: "))
number2 = int(input("Enter the upper bound: "))

random_number = random.randint(number1, number2)
print(f"Random number between {number1} and {number2}: {random_number}")