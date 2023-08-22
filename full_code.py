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
    try:
        with open(input_filename, 'w') as file:
            for value in values:
                file.write(str(value) + '\n')
        print("Values stored in the file successfully.")
    except Exception as e:
        print("An error occurred while storing values:", e)

# Function to read values from the file and create a graph
def read_values_and_plot():
    values = []
    try:
        with open(input_filename, 'r') as file:
            for line in file:
                values.append(float(line.strip()))

        plt.plot(values, marker='o')
        plt.xlabel('Data Point')
        plt.ylabel('Value')
        plt.title('Graph of Input Values')
        plt.show()
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid value found in the file.")

# Function to retrieve data from an API
def get_data_from_api():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad requests
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching data from the API:", e)
        return None

# Function to perform pandas operations
def perform_pandas_operations(data):
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)
    print("")
    print("Mean Age:", df['Age'].mean())
    print("")
    print("Max Score:", df['Score'].max())
    print("")
    print("Rows with Age > 25:")
    print(df[df['Age'] > 25])
    print("")
    sorted_df = df.sort_values(by='Score', ascending=False)
    print("Sorted DataFrame by Score:")
    print(sorted_df)
    print("")

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
