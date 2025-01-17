import random

# Generate a list of 100 random numbers between 100 and 900
random_numbers = [random.randint(100, 900) for _ in range(100)]

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Separate odd, even, and prime numbers
odd_numbers = [num for num in random_numbers if num % 2 != 0]
even_numbers = [num for num in random_numbers if num % 2 == 0]
prime_numbers = [num for num in random_numbers if is_prime(num)]

# Print results
print(f"Odd Numbers ({len(odd_numbers)}): {odd_numbers}")
print(f"Even Numbers ({len(even_numbers)}): {even_numbers}")
print(f"Prime Numbers ({len(prime_numbers)}): {prime_numbers}")
