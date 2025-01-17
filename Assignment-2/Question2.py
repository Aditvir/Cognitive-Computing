scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

# i. Identify the highest score and its index in the tuple
highest_score = max(scores)
highest_index = scores.index(highest_score)
print(f"Highest score: {highest_score}, Index: {highest_index}")

# ii. Find the lowest score and count how many times it appears
lowest_score = min(scores)
count_lowest = scores.count(lowest_score)
print(f"Lowest score: {lowest_score}, Count: {count_lowest}")

# iii. Reverse the tuple and return it as a list
reversed_list = list(scores[::-1])
print(f"Reversed tuple as list: {reversed_list}")

# iv. Check if a specific score '76' (input by the user) is present in the tuple
score_to_check = float(input("Enter a score to check: "))
if score_to_check in scores:
    first_occurrence_index = scores.index(score_to_check)
    print(f"Score {score_to_check} is present at index {first_occurrence_index}.")
else:
    print(f"Score {score_to_check} is not present in the tuple.")
