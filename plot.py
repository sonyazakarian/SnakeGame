

import matplotlib.pyplot as plt

# Data
input_size = [5000, 10000, 20000, 40000, 80000]
sequential_search = [0.40619, 1.69064, 6.60075, 25.70789, 110.854]
binary_search = [0.00324, 0.00715, 0.01568, 0.03366, 0.07013]
two_pointer_search = [0.00024, 0.00046, 0.00092, 0.00183, 0.00375]

# Create the plot
plt.figure(figsize=(8,6))
plt.plot(input_size, sequential_search, label="Sequential Search", marker='o')
plt.plot(input_size, binary_search, label="Binary Search", marker='o')
plt.plot(input_size, two_pointer_search, label="Two-pointer Search", marker='o')

# Adding labels and title
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Comparison of Search")

