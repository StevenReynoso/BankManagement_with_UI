# BankManagement_with_UI
BankManagement app that displays employees and can update their status using tkinter and mysql

# Employee Management System

This is a simple Employee Management System implemented using Python and Tkinter for the GUI. The program allows you to add, promote, remove, and display employees in a MySQL database.

<img width="300" alt="4dbe77b04039effe64d785b8c0b2d19b" src="https://github.com/StevenReynoso/BankManagement_with_UI/assets/114453891/1889a7b3-a213-48ed-8f16-2c8e2bf8626f">

<img width="300" alt="1f3f29ad925409c7429a2b5c3e6c1e80" src="https://github.com/StevenReynoso/BankManagement_with_UI/assets/114453891/36e88a89-6dda-44e2-96b4-33a33034c089">

## Prerequisites

- Python 3.x
- MySQL database server

## Installation

1. Clone the repository:

git clone https://github.com/StevenReynoso/employee-management-system.git

Install the required packages:

     pip install mysql-connector-python

Modify the database connection details in the code (main.py) to match your MySQL server settings:
    
    con = mysql.connector.connect(
    host="localhost",
    user="sqluser",
    password="password",
    database="bankdb")

## Usage

Run the program by executing main.py:

    PythonBankManagement.py

The GUI application will open, allowing you to interact with the Employee Management System.
Features

Add new employees with their credentials.
Promote employees by updating their position and salary.
Remove employees from the database.
Display a list of employees in a tabular format.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.
