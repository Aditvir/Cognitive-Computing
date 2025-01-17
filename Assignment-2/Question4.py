# Define the sets
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# i. Find the unique scores achieved by both teams (union of sets)
union_set = A.union(B)
print(f"Unique scores (Union of sets A and B): {union_set}")

# ii. Identify the scores that are common to both teams (intersection of sets)
intersection_set = A.intersection(B)
print(f"Common scores (Intersection of sets A and B): {intersection_set}")

# iii. Find the scores that are exclusive to each team (symmetric difference)
symmetric_difference_set = A.symmetric_difference(B)
print(f"Exclusive scores (Symmetric Difference): {symmetric_difference_set}")

# iv. Check if the scores of team A are a subset of team B, and if team B's scores are a superset of team A
is_subset = A.issubset(B)
is_superset = B.issuperset(A)
print(f"Are A's scores a subset of B? {is_subset}")
print(f"Are B's scores a superset of A? {is_superset}")

# v. Remove a specific score X from set A if it exists, else print a message
X = int(input("Enter a score to remove from set A: "))
if X in A:
    A.remove(X)
    print(f"Score {X} removed from set A.")
else:
    print(f"Score {X} not found in set A.")
