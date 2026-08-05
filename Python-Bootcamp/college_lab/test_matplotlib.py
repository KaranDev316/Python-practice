import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Marks": [78, 92, 65, 88, 95]
}

df = pd.DataFrame(data)

print(df)

plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks")
plt.ylabel("Marks")
plt.show()