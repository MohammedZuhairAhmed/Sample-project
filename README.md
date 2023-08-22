# Simple Data Analysis and Visualization

This is a simple Python program that demonstrates data analysis and visualization concepts using the `requests` library for API requests, `pandas` library for data manipulation, and `matplotlib` library for plotting.

## Features

1. **Store Input Values and Plot**
    - Allows users to input values and store them in a file.
    - Reads the stored values from the file and creates a line plot using `matplotlib`.

2. **Retrieve Data from API**
    - Makes a GET request to an API using the `requests` library.
    - Prints sample data from the API response.

3. **Perform Pandas Operations**
    - Demonstrates basic data manipulation using the `pandas` library.
    - Calculates mean age and max score, filters rows with age > 25, and sorts the DataFrame by score.

4. **Menu Interface**
    - Utilizes an interactive menu interface for users to select different actions.

## Instructions

1. Install project dependencies using the following command:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the script using a Python interpreter: 
    ```bash
    python main.py
    ```

3. Follow the on-screen instructions to perform different operations.
4. The menu allows you to choose between storing input values, retrieving data from an API, performing pandas operations, or exiting the program.

## Dependencies

- Python 3.x
- Required libraries:
  - `requests`
  - `pandas`
  - `matplotlib`
