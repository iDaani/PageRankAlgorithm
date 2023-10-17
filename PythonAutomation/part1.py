import matplotlib.pyplot as plt

def main():

    # Replace 'data.txt' with the path to your text file
    file_path = 'C:/Users/Pranay/OneDrive/Desktop/PythonProj/csr.txt'
    coo_file_path = 'C:/Users/Pranay/OneDrive/Desktop/PythonProj/coo.txt'
    csc_file_path = 'C:/Users/Pranay/OneDrive/Desktop/PythonProj/csc.txt'

    # Initialize an empty list to store the residual error values
    # Create an empty list to store the numbers
    numbers = []

    # Fill the list with numbers from 1 to 53
    for i in range(1, 59):
        numbers.append(i)

    csr = []
    coo = []
    csc = []

    # Read data from the text file and extract residual error values
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by spaces
            parts = line.split()
            for part in parts:
                if 'error' in part:
                    # Extract the residual error value (skip the 'residual' and 'error=')
                    trying = part.split('=')
                    residual_error = float(part.split('=')[1])
                    csr.append(residual_error)

    # Read data from the text file and extract residual error values
    with open(coo_file_path, 'r') as file:
        for line in file:
            # Split the line by spaces
            parts = line.split()
            for part in parts:
                if 'error' in part:
                    # Extract the residual error value (skip the 'residual' and 'error=')
                    trying = part.split('=')
                    residual_error = float(part.split('=')[1])
                    coo.append(residual_error)

    # Read data from the text file and extract residual error values
    with open(csc_file_path, 'r') as file:
        for line in file:
            # Split the line by spaces
            parts = line.split()
            for part in parts:
                if 'error' in part:
                    # Extract the residual error value (skip the 'residual' and 'error=')
                    trying = part.split('=')
                    residual_error = float(part.split('=')[1])
                    csc.append(residual_error)

# # Print the list of residual error values
#     print(csr)
#     print(coo)
#     print(csc)
#     print(numbers)

    # Create a log-scale plot with multiple lines
    plt.figure(figsize=(10, 6))
    # plt.semilogx(numbers, csr, marker='o', linestyle='-', color='b', label='CSR Data')
    # plt.semilogx(numbers, csc, marker='o', linestyle='-', color='r', label='CSC Data')
    plt.semilogx(numbers, coo, marker='o', linestyle='-', color='y', label='COO Data')
    # You can add more lines for additional columns if needed

    plt.title('Residual Error for COO method')
    plt.xlabel('Number of Iterations (log scale)')
    plt.ylabel('Residual Error')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
