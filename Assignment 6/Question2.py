import pandas as pd
import random

data = {
    'Subject': ['Biology', 'Chemistry', 'Literature', 'Economics', 'Computer Science'],
    'Scores': [random.randint(50, 100) for _ in range(5)]
}

df = pd.DataFrame(data)
df

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
ax = sns.barplot(x='Subject', y='Scores', data=df, hue='Subject', palette='coolwarm', legend=False)

for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                xytext=(0, 5), textcoords='offset points',
                ha='center', va='center', fontsize=10, color='black')

plt.title('Student Scores in Different Subjects')
plt.xlabel('Subject')
plt.ylabel('Scores')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
