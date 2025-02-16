import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales_df = pd.read_csv('company_sales_data.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(x='month_number', y='total_profit', data=sales_df)

plt.title('Monthly Profit Trends')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
for item in ['sunscreen', 'bodywash', 'toothbrush', 'handsoap', 'conditioner', 'lotion']:
    sns.lineplot(x='month_number', y=item, data=df, label=item)

plt.title('Sales Data of Various Products')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 8))
for column in df.columns[1:]:
    plt.figure(figsize=(8, 6))
    sns.barplot(x=df.index, y=column, data=df, palette="coolwarm")
    plt.xlabel('Data Index')
    plt.ylabel(column)
    plt.xticks(rotation=30)
    plt.title(f'Distribution of {column}')
    plt.grid(axis='y', linestyle='dashed', alpha=0.6)
    plt.show()