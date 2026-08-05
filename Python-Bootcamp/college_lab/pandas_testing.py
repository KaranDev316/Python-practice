import pandas as pd

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)

print("Pandas version:", pd.__version__)
print("\nDataFrame:")
print(df)