iris_df = iris_df.drop(iris_df.index[4])
iris_df = iris_df.drop(iris_df.columns[3], axis=1)

print(iris_df.head())