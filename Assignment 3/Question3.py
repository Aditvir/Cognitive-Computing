import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

# (i) Select rows from index 3 to 7
rows_3_to_7 = df.iloc[3:8]

print("Rows from index 3 to 7:")
print(rows_3_to_7)

# (ii) Select row from index 4 to 8, and column 2 to 4.
rows_4_to_8_cols_2_to_4 = df.iloc[4:9, 2:5]

print("\nRows from index 4 to 8, and columns 2 to 4:")
print(rows_4_to_8_cols_2_to_4)

# (iii) Select all rows with column index 1 to 3 (include index 3 during selection)
cols_1_to_3 = df.iloc[:, 1:4]

print("\nAll rows with column index 1 to 3:")
print(cols_1_to_3)

