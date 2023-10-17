import matplotlib.pyplot as plt
# Define your X-axis values
x_values = [55.557274599, 71.1748189, 200.1620197]

# Choose Y-values for an increasing linear relationship
y_values = [50, 100, 150]

# Create a scatter plot
plt.scatter(x_values, y_values, label='Data Points', color='blue')


# Set labels for the axes
plt.xlabel('Execution time taken (in seconds)')
plt.ylabel('Time elapsed (in seconds)')

# Set a title for the plot
plt.title('Scatter Plot of Execution Time of CSR, CSC and COO algorithms')

# Add labels for the points
for i in range(len(x_values)):
    if i == 0:
        plt.text(x_values[i], y_values[i], f'CSR time: {x_values[i]:.2f}s', fontsize=10, ha='left', va='bottom')
    if i == 1:
        plt.text(x_values[i], y_values[i], f'CSC time: {x_values[i]:.2f}s', fontsize=10, ha='left', va='bottom')
    if i == 2:
        plt.text(x_values[i], y_values[i], f'COO time: {x_values[i]:.2f}s', fontsize=10, ha='left', va='bottom')

# # Add lines connecting the points
plt.plot(x_values, y_values, 'r--', label='Connect Points')

# Add a legend
plt.legend()

# Display the plot
plt.grid
plt.show()