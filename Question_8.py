# 8.1 Handle division by zero:
try:
    print(38 / 0)
except ZeroDivisionError:
    print("Cannot be divided by zero. Please enter a valid input")

# 8.2 Handle invalid input:
try:
    num = int(input("provide a number: "))
except ValueError:
    print("Invalid input")

# 8.3 Use finally:
try:
    print(38 / 2)
finally:
    print("This will always execute.")