import pandas as pd

df = pd.read_csv("students.csv")

print(df)
print("\nFirst two rows:")
print(df.head(2))
print("\nLast two rows:")
print(df.tail(2))


print("\nColumn names:")
print(df.columns)