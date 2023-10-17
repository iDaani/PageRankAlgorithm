# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Replace 'your_file.csv' with the path to your CSV file
# file_path = 'C:/Users/Pranay/OneDrive/Desktop/PythonProj/Error rate(1).csv'
#
# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(file_path)
#
# # Assuming your CSV has two columns named 'x' and 'y'
# x = df['CSR']
# y = df['COO']
#
# # Create a log-scale plot
# plt.figure(figsize=(10, 6))
# plt.semilogx(x, y, marker='o', linestyle='-', color='b', label='Data')
# plt.title('Log-Scale Chart')
# plt.xlabel('X-axis (log scale)')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.legend()
# plt.show()
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Replace 'your_file.csv' with the path to your CSV file
# file_path = 'C:/Users/Pranay/OneDrive/Desktop/PythonProj/Error rate(1).csv'
#
# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(file_path)
#
# # Assuming your CSV has three columns named 'x', 'y1', and 'y2'
# x = df['CSR']
# y1 = df['COO']
# y2 = df['CSC']
# y3 = df['CSC FLOAT']
#
# # Create a log-scale plot with multiple lines
# plt.figure(figsize=(10, 6))
# plt.semilogx(x, y1, marker='o', linestyle='-', color='b', label='Y1 Data')
# plt.semilogx(x, y2, marker='o', linestyle='-', color='r', label='Y2 Data')
# plt.semilogx(x, y3, marker='o', linestyle='-', color='y', label='Y3 Data')
# # You can add more lines for additional columns if needed
#
# plt.title('Log-Scale Chart with Multiple Lines')
# plt.xlabel('X-axis (log scale)')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt

# Replace 'data.txt' with the path to your text file
file_path = 'C:/Users/Pranay/OneDrive/Desktop/PythonProj/new.txt'

# Initialize empty lists for each column
x = []
y1 = []
y2 = []

# Read data from the text file
with open(file_path, 'r') as file:
    next(file)  # Skip the header row if present
    for line in file:
        data = line.split()
        x.append(float(data[0]))
        y1.append(float(data[1]))
        y2.append(float(data[2]))

# Create a log-scale plot with multiple lines
plt.figure(figsize=(10, 6))
plt.semilogx(x, y1, marker='o', linestyle='-', color='b', label='Y1 Data')
plt.semilogx(x, y2, marker='o', linestyle='-', color='r', label='Y2 Data')
# You can add more lines for additional columns if needed

plt.title('Log-Scale Chart with Multiple Lines')
plt.xlabel('X-axis (log scale)')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()
plt.show()
