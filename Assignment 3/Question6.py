import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5],
}

df = pd.DataFrame(data)

# a) Shape of the DataFrame
print("Shape of the DataFrame:", df.shape)

# b) Summary of the DataFrame
print("\nSummary of the DataFrame:")
print(df.info())

# c) Generate descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# d) Display first 5 rows and last 3 rows
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 3 rows:")
print(df.tail(3))

# e) Calculate statistics
print("\nAverage salary of employees:", df["Salary"].mean())
print("Total bonus paid to all employees:", df["Bonus"].sum())
print("Youngest employee's age:", df["Age"].min())
print("Highest performance rating:", df["Rating"].max())

# f) Sort by Salary in descending order
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nDataFrame sorted by Salary (descending):")
print(sorted_df)

# g) Add a new column categorizing employees based on rating
def categorize_rating(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Performance"] = df["Rating"].apply(categorize_rating)
print("\nDataFrame with Performance category:")
print(df)

# h) Identify missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# i) Rename Employee_ID to ID
df.rename(columns={"Employee_ID": "ID"}, inplace=True)
print("\nDataFrame after renaming Employee_ID to ID:")
print(df)

# j) Find employees with:
#    i. More than 5 years of experience
print("\nEmployees with more than 5 years of experience:")
print(df[df["Years_of_Experience"] > 5])

#    ii. Belong to the IT department
print("\nEmployees in the IT department:")
print(df[df["Department"] == "IT"])

# k) Add a new column, Tax (10% of Salary)
df["Tax"] = df["Salary"] * 0.10
print("\nDataFrame with Tax column:")
print(df)

# l) Save the modified DataFrame to a new CSV file
output_file = "modified_employees.csv"
df.to_csv(output_file, index=False)
print(f"\nModified DataFrame saved to {output_file}")
