# 6.1 Count number of vowels:
s = "King henry disliked the taste of the meal"
print(sum(1 for c in s.lower() if c in "aeiou"))

# 6.2 Reverse a string:
s = "constructive criticism"
print(s[::-1])

# 6.3 Check if a string is a palindrome:
s = "rotator"
print(s == s[::-1])