# 9.1 Generate 5 random numbers:
import random
print("5 random numbers are ",[random.randint(1, 100) for _ in range(5)])

# 9.2 Check if random number is prime:
import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = random.randint(1, 100)
print(f"Generated number: {num}")
print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")

# 9.3 Simulate rolling a die:
print("The rolled number is ", random.randint(1, 6))

# 9.4 Shuffle a list:
numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)
print(numbers)

# 9.5 Randomly select an item:
print(random.choice([10, 20, 30, 40, 50, 60, "car", "bike", "bus" ]))

# 9.6 Generate random password:
import string
length = 6
print("".join(random.choices(string.ascii_letters + string.digits, k=length)))

# 9.7 Pick a random card:
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
values = ["Ace" ,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
print(random.choice(values) + " of " + random.choice(suits))