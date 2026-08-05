import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y, marker='o')
plt.title("My First Matplotlib Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

# Display the graph
plt.show()

print("Matplotlib is working!")