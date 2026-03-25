import pandas as pd

data = pd.read_csv("students.csv")

print("First 5 Rows of Dataset:")
print(data.head())

print("\nShape of the Dataset:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nStatistical Summary:")
print(data.describe())

print("\nMissing Values in Each Column:")
print(data.isnull().sum())