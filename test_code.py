import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define constants
input_filename = "input_values.txt"
api_url = "https://jsonplaceholder.typicode.com/posts"
data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 22, 28, 23],
        'Score': [85, 90, 78, 95, 88]
}

# Function to store values in a file
def store_values_in_file(values):
    """
    Store the provided values in a file named 'input_values.txt'.
    """
    # Implement code here to open the file and write values
    
    print("Values stored in the file successfully.")

# Function to read values from the file and create a graph
def read_values_and_plot():
    """
    Read values from the 'input_values.txt' file and create a plot.
    """
    # Implement code here to open the file, read values, and create a plot

# Function to retrieve data from an API
def get_data_from_api():
    """
    Retrieve data from the provided API URL.
    """
    # Implement code here to make a GET request to the API and return the data

# Function to perform pandas operations
def perform_pandas_operations(data):
    """
    Perform basic pandas operations on the provided data.
    """
    # Implement code here to create a DataFrame from the provided data
    # Calculate mean age and max score
    # Filter rows with age > 25
    # Sort DataFrame by score

def main():
    while True:
        print("\nMenu:")
        print("1. Store input values in a file and plot")
        print("2. Retrieve data from API")
        print("3. Perform pandas operations")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("")
            num_inputs = int(input("Enter the number of data points: "))
            input_values = []
            for i in range(num_inputs):
                value = float(input(f"Enter value {i + 1}: "))
                input_values.append(value)
            store_values_in_file(input_values)
            read_values_and_plot()
        
        elif choice == "2":
            print("")
            api_data = get_data_from_api()
            if api_data:
                print("Sample data from API:")
                for entry in api_data[:5]:
                    print("")
                    print("Title:", entry["title"])
                    print("Body:", entry["body"])
                    print("")
                    print("=" * 50)
        
        elif choice == "3":
            print("")
            perform_pandas_operations(data)
        
        elif choice == "4":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
