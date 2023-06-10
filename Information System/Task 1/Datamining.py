import pandas as pd

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Filter data based on a condition
filtered_data = data[data['age'] > 30]

# Group data by a specific column and calculate the average of another column
grouped_data = filtered_data.groupby('occupation')['income'].mean()

# Sort the grouped data in descending order
sorted_data = grouped_data.sort_values(ascending=False)

# Display the top 5 results
top_5 = sorted_data.head(5)
print("Top 5 occupations with highest average income:")
print(top_5)