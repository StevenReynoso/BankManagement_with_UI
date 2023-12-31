# BankManagement_with_UI
BankManagement app that displays employees and can update their status using tkinter and mysql

# Employee Management System

This is a simple Employee Management System implemented using Python and Tkinter for the GUI. The program allows you to add, promote, remove, and display employees in a MySQL database.
<a href="https://gyazo.com/af2ac32d0b5671cc7a8eaa426ff853be"><img src="https://i.gyazo.com/af2ac32d0b5671cc7a8eaa426ff853be.png" alt="Image from Gyazo" width="796.6666666666666"/></a>
<a href="https://gyazo.com/689e7b4139e441c43e02b54cf103c9fc"><img src="https://i.gyazo.com/689e7b4139e441c43e02b54cf103c9fc.jpg" alt="Image from Gyazo" width="610.6666666666666"/></a>


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
