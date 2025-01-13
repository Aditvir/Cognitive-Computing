# 5.1 Find largest and smallest in a list:
numbers = [21, 8, 65, 43, 29]
print(max(numbers), min(numbers))


# 5.2 Retrieve value from a dictionary:
d = {"x": 10, "y": 20, "z": 30}
print(d["z"])

# 5.3 Sort a list:
numbers = [22, 9, 66, 44, 30]
print(sorted(numbers))  # In  Ascending order
print(sorted(numbers, reverse=True))  # In Descending order


# 5.4 Merge dictionaries:
d1 = {"a": 10, "b": 20}
d2 = {"x": 30, "y": 40}
d1.update(d2)
print(d1)