from BankClasses import *
import tkinter as tk

window.title("Bank Management")
window.geometry("800x600")
frame = tk.Frame(window)
frame.grid()  # Use grid() for the frame


def add_emp():
    frame.grid_remove()
    Add_emptk(show_main_menu)

def show_main_menu():
    frame.grid()
    add_frame.grid_forget()
    promote_frame.grid_forget()
    remove_frame.grid_forget()
    display_frame.grid_forget()


def promote_emp():
    frame.grid_remove()
    promote_emptk(show_main_menu)
    
def remove_emp():
    frame.grid_remove()
    Remove_Employee(show_main_menu)
    
def display_emp():
    frame.grid_remove()
    Display_Employees(show_main_menu)

def show_add_emp():
    frame.grid_remove()
    MainMenu()

# widgets
def MainMenu():
    lbl = tk.Label(frame, text="Welcome to Bank Management Services", fg='black', font=("Helvetica", 18))
    lbl.grid(column = 1, columnspan = 3, padx = 200, sticky = "n")  # Use grid() for labels

    btn_add = tk.Button(frame, text="Add Employee", width = 25, fg = 'blue', font = ("Helvetica", 12), command = add_emp)
    btn_add.grid(row = 1, column = 2, columnspan = 1)

    btn_promote = tk.Button(frame, text = "Promote Employee", width = 25, fg = 'blue', font = ("Helvetica", 12), command = promote_emp)
    btn_promote.grid(row = 2, column = 2, columnspan = 1)

    btn_remove = tk.Button(frame, text = "Remove Employee", width = 25, fg = 'blue', font = ("Helvetica", 12), command = remove_emp)
    btn_remove.grid(row = 3, column = 2, columnspan = 1)

    btn_display = tk.Button(frame, text = "Display Employees", width = 25, fg = 'blue', font = ("Helvetica", 12), command = display_emp)
    btn_display.grid(row = 4, column = 2, columnspan = 1)

MainMenu()
window.mainloop()