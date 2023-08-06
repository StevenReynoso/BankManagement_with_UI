import mysql.connector
import tkinter as tk


con = mysql.connector.connect(
    host = "localhost", user = "sqluser", password = "password", database = "bankdb"
)

window = tk.Tk()
add_frame = tk.Frame()
promote_frame = tk.Frame()
remove_frame = tk.Frame()
display_frame = tk.Frame()

def Add_emptk(callback):
    add_frame.grid()
    lbl = tk.Label(add_frame, text="Enter New Employee's Credentials", font=("Arial", 16))
    lbl.grid(row = 0, column = 1, columnspan=3, padx = 150, sticky = "n")  # Spanning two columns for the title label
    
    lbl_id = tk.Label(add_frame, text="ID Number", font=("Arial", 12))
    lbl_Fname = tk.Label(add_frame, text="First Name", font=("Arial", 12))
    lbl_Lname = tk.Label(add_frame, text="Last Name", font=("Arial", 12))
    lbl_pos = tk.Label(add_frame, text="Position", font=("Arial", 12))
    lbl_sal = tk.Label(add_frame, text="Salary", font=("Arial", 12))
    
    lbl_id.grid(row = 1, column = 2, sticky = "w")  # Align right ("e" for east)
    lbl_Fname.grid(row = 2, column = 2, sticky = "w")
    lbl_Lname.grid(row = 3, column = 2, sticky = "w")
    lbl_pos.grid(row = 4, column = 2, sticky = "w")
    lbl_sal.grid(row = 5, column = 2, sticky = "w")

    id_entry = tk.Entry(add_frame)
    id_entry.grid(row = 1, column = 2)

    Fname_entry = tk.Entry(add_frame)
    Fname_entry.grid(row = 2, column = 2)

    Lname_entry = tk.Entry(add_frame)
    Lname_entry.grid(row = 3, column = 2)

    pos_entry = tk.Entry(add_frame)
    pos_entry.grid(row = 4, column = 2)

    sal_entry = tk.Entry(add_frame)
    sal_entry.grid(row = 5, column = 2)

    result_label = tk.Label(add_frame, text="", font=("Arial", 12))
    result_label.grid(row = 7, column = 2, columnspan=2)

    def on_add_employee():
        Id = id_entry.get()
        Fname = Fname_entry.get()
        Lname = Lname_entry.get()
        pos = pos_entry.get()
        sal = sal_entry.get()

         #add a check if it already exists
        if check_employee(Id):
            result_label.config(text="Employee ID Already Exists, Please Try Again!", fg="red")
        else:
            result_label.config(text="Employee Added Successfully", fg="green")
            Add_Employee(Id, Fname, Lname, pos, sal)

    btn_add_employee = tk.Button(add_frame, text = "Submit", fg = 'black', font = ("Helvetica", 10), command = on_add_employee)
    btn_add_employee.grid(row = 6, column = 2, padx = 100, sticky = "w")
    btn_back = tk.Button(add_frame, text = "Back", fg = "black", font = ("Helvetica", 10), command = callback)
    btn_back.grid(row = 6, column = 2, pady = 5)

def promote_emptk(callback):
    promote_frame.grid()
    lbl = tk.Label(promote_frame, text = "Enter ID of Employee to Promote", font = ("Arial", 16))
    lbl.grid(row = 0, column = 2, columnspan = 3, padx = 250, pady = 10)  # Spanning two columns for the title label
    lbl_id = tk.Label(promote_frame, text = "ID", font = ("Arial", 12))
    lbl_id.grid(row = 1, column = 3, padx = 100, sticky = "w" )  # Align right ("e" for east)
    lbl_info = tk.Label(promote_frame, text = "Employee Info", font = ("Arial", 12))
    lbl_info.grid(row = 2, column = 3, padx = 20, sticky = "w")
    lbl_new_pos = tk.Label(promote_frame, text = "New Position", font = ("Arial", 12))
    lbl_new_pos.grid(row = 6, column = 3, padx = 20, sticky = "w" )  # Align right ("e" for east)
    lbl_new_sal = tk.Label(promote_frame, text = "New Salary", font = ("Arial", 12))
    lbl_new_sal.grid(row = 7, column = 3, padx = 20, sticky = "w")


    id_entry = tk.Entry(promote_frame)
    id_entry.grid(row = 1, column = 3, pady = 25)
    Fname_entry = tk.Entry(promote_frame)
    Fname_entry.grid(row = 2, column = 3)
    Lname_entry = tk.Entry(promote_frame)
    Lname_entry.grid(row = 3, column = 3)
    pos_entry = tk.Entry(promote_frame)
    pos_entry.grid(row = 4, column = 3)
    sal_entry = tk.Entry(promote_frame)
    sal_entry.grid(row = 5, column = 3)

    New_pos_entry = tk.Entry(promote_frame)
    New_pos_entry.grid(row = 6, column = 3, pady = 10)
    New_sal_entry = tk.Entry(promote_frame)
    New_sal_entry.grid(row = 7, column = 3, pady = 10)

    def On_Promote():
        new_pos = New_pos_entry.get()
        new_sal = New_sal_entry.get()
        Id = id_entry.get()
        Promote_Employee(new_pos, new_sal, Id)
        result_label.config(text = "Employee Promoted", fg = "green")

    def on_search():
        Id = id_entry.get()

        if not check_employee(Id):
            result_label.config(text="Employee ID Does Not Exist, Please Try Again!", fg = "red")
        else:
            find_employee(Id, Fname_entry, Lname_entry, pos_entry, sal_entry)
            result_label.config(text="Employee Found", fg = "green")

    search_btn = tk.Button(promote_frame, width = 10, text = "Search", font = ("Arial", 12), command = on_search)
    search_btn.grid(row = 8, column = 3, sticky = "w")
    prom_btn = tk.Button(promote_frame, width = 10, text = "Promote", font = ("Arial", 12), command = On_Promote)
    prom_btn.grid(row = 8, column = 3, sticky = "e")
    back_btn = tk.Button(promote_frame, text = "Back", font = ("Arial", 12), command = callback )
    back_btn.grid(row = 8, column = 3, sticky = "s")

    result_label = tk.Label(promote_frame, text="", font=("Arial", 12))
    result_label.grid(row = 9, column = 3)


#Checks Employees id to see if it exists already.
def check_employee(employee_id):
    sql = 'SELECT * from employees WHERE Personid = %s'
    c = con.cursor(buffered = True) #buffer cursor to work properly
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount

    if r == 1:
        return True
    else:
        return False

def find_employee(id, Fname_entry, Lname_entry, pos_entry, sal_entry):
    sql = 'SELECT * from employees WHERE Personid = %s'
    c = con.cursor()
    data = (id,)
    c.execute(sql, data)
    r = c.fetchall()

    Fname_entry.delete(0, "end")
    Lname_entry.delete(0, "end")
    pos_entry.delete(0, "end")
    sal_entry.delete(0, "end")

    for i in r:
        Lname_entry.insert(0, i[1])
        Fname_entry.insert(0, i[2])
        pos_entry.insert(0, i[3])
        sal_entry.insert(0, i[4])
       

def Add_Employee(Id, Fname, Lname, pos, sal):
   
        data = (Fname, Lname, Id, pos, sal)

        #insert into table
        sql = 'INSERT INTO employees(FirstName, LastName, Personid, Position, Salary) VALUES(%s, %s, %s, %s, %s)'
        c = con.cursor()
        c.execute(sql, data)    # executing the query
        con.commit()
        print("Employee Added Successfully")    #success message
        

def Promote_Employee(new_pos, Amount, Id):
    #second check
    if(not check_employee(Id)):
        print("Employee does not exists \nPlease Try Again\n")
        promote_emptk()

    else:
        sql = 'SELECT Position, Salary from employees where Personid = %s'
        data = (Id,)
        c = con.cursor(buffered = True) 
        c.execute(sql, data)
        r = c.fetchone()

        sql = 'UPDATE employees set Salary = %s, Position = %s where Personid = %s'
        d = (Amount, new_pos, Id)
        c.execute(sql, d)
        con.commit()

        print("Employee Promoted")

def Remove_Employee(callback):
    remove_frame.grid()
    lbl = tk.Label(remove_frame, text = "Enter ID of Employee to Remove", font = ("Arial", 16))
    lbl.grid(row = 0, column = 2, columnspan = 3, padx = 250, pady = 10) 
    lbl_id = tk.Label(remove_frame, text = "ID", font = ("Arial", 12))
    lbl_id.grid(row = 1, column = 3, padx = 100, sticky = "w" ) 
    lbl_info = tk.Label(remove_frame, text = "Employee Info", font = ("Arial", 12))
    lbl_info.grid(row = 2, column = 3, padx = 20, sticky = "w")
    
    id_entry = tk.Entry(remove_frame)
    id_entry.grid(row = 1, column = 3, pady = 25)
    Fname_entry = tk.Entry(remove_frame)
    Fname_entry.grid(row = 2, column = 3)
    Lname_entry = tk.Entry(remove_frame)
    Lname_entry.grid(row = 3, column = 3)
    pos_entry = tk.Entry(remove_frame)
    pos_entry.grid(row = 4, column = 3)
    sal_entry = tk.Entry(remove_frame)
    sal_entry.grid(row = 5, column = 3)

    def On_Remove():
        Id = id_entry.get()

        #Second Check
        if not check_employee(Id):
            result_label.config(text="Employee ID Does Not Exist, Please Try Again!", fg = "red")
        
        else:
            sql = 'DELETE from employees WHERE Personid = %s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            result_label.config(text="Employee Has Been Removed", fg = "Green")

    def on_search():
        Id = id_entry.get()

        if not check_employee(Id):
            result_label.config(text="Employee ID Does Not Exist, Please Try Again!", fg = "red")
        else:
            find_employee(Id, Fname_entry, Lname_entry, pos_entry, sal_entry)
            result_label.config(text="Employee Found", fg = "green")

    search_btn = tk.Button(remove_frame, width = 10, text = "Search", font = ("Arial", 12), command = on_search)
    search_btn.grid(row = 8, column = 3, sticky = "w")
    remove_btn = tk.Button(remove_frame, width = 10, text = "Remove", font = ("Arial", 12), command = On_Remove)
    remove_btn.grid(row = 8, column = 3, sticky = "e")
    back_btn = tk.Button(remove_frame, text = "Back", font = ("Arial", 12), command = callback )
    back_btn.grid(row = 8, column = 3, sticky = "s")

    result_label = tk.Label(remove_frame, text="", font=("Arial", 12))
    result_label.grid(row = 9, column = 3)


def Display_Employees(callback):
    display_frame.grid()
    sql = 'select * from employees'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()

    lbl = tk.Label(display_frame, text="Employee List", font=("Arial", 16))
    lbl.grid(row = 0, column = 3, columnspan = 2)
    
    # Column headers
    headers = ["ID", "Last Name", "First Name", "Position", "Salary"]
    for col, header_text in enumerate(headers, start = 1):
        lbl = tk.Label(display_frame, text = header_text, font = ("Arial", 12))
        lbl.grid(row = 1, column = col, columnspan = 1)

    # Create labels to display employee data
    for row_index, employee in enumerate(r, start=2):
        for col_index, value in enumerate(employee):
            label = tk.Label(display_frame, text = value, width = 15)
            label.grid(row = row_index, column = col_index + 1)  # Start at column 1 to skip the header column

    back_btn = tk.Button(display_frame, text = "Back", font = ("Arial", 12), command = callback)
    back_btn.grid(row = len(r) + 2, column = 2, columnspan = 2, pady = 10)
