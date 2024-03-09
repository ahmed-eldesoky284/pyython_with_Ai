import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("student_data.csv")

print("Columns in the dataset: ", data.columns)

data.dropna(inplace=True)

your_threshold = 1000

data = data[data['Age'] < your_threshold]

plt.figure(figsize=(10,6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(10,6))
sns.scatterplot(x='availability', y='Age', data=data)
plt.title('Age vs. Availability')
plt.xlabel('Availability')
plt.ylabel('Age')
plt.show()

correlation_matrix = data.corr()
print(correlation_matrix)

plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()



