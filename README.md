# BankManagement_with_UI
BankManagement app that displays employees and can update their status using tkinter and mysql

# Employee Management System

This is a simple Employee Management System implemented using Python and Tkinter for the GUI. The program allows you to add, promote, remove, and display employees in a MySQL database.

## Prerequisites

- Python 3.x
- MySQL database server

## Installation

1. Clone the repository:

git clone https://github.com/StevenReynoso/employee-management-system.git

    Install the required packages:

bash

pip install mysql-connector-python

    Modify the database connection details in the code (main.py) to match your MySQL server settings:

python

con = mysql.connector.connect(
    host="localhost",
    user="sqluser",
    password="password",
    database="bankdb"
)

Usage

Run the program by executing main.py:

bash

python main.py

The GUI application will open, allowing you to interact with the Employee Management System.
Features

    Add new employees with their credentials.
    Promote employees by updating their position and salary.
    Remove employees from the database.
    Display a list of employees in a tabular format.

Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.
```bash
