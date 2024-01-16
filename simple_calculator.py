import tkinter as tk
from tkinter import ttk

#defining function of addition
def add(x, y):
    return x + y

#defining function of substraction
def subtract(x, y):
    return x - y

#defining function of multiplication
def multiply(x, y):
    return x * y

#defining function of division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        result_window = tk.Toplevel(root)
        result_window.title("Result")
        
        label_result = ttk.Label(result_window, text=f"Result: {result}")
        label_result.grid(row=0,column=0,padx=10,pady=10)

    except ValueError:
        ttk.showerror("Error", "Invalid input. Please enter valid numbers.")

def clear_inputs():
    entry_num1.delete(0, ttk.END)
    entry_num2.delete(0, ttk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator App")

#Create entry widge for input
label_num1=ttk.Label(root,text="Enter number 1:")
label_num1.grid(row=0,column=0,padx=10,pady=10)

entry_num1 = ttk.Entry(root, font=('calibri', 12, 'bold'), justify='center')
entry_num1.grid(row=0,column=1,padx=10,pady=10)

label_num2=ttk.Label(root,text="Enter number 2:")
label_num2.grid(row=1,column=0,padx=10,pady=10)

entry_num2 = ttk.Entry(root, font=('calibri', 12, 'bold'), justify='center')
entry_num2.grid(row=1,column=1,padx=10,pady=10)

# Operation dropdown
label_select_operation=ttk.Label(root,text="Select Operation to perform")
label_select_operation.grid(row=2,column=0,padx=10,pady=10)
operations = ["Addition +", "Subtraction -", "Multiplication *", "Division /"]
operation_var = tk.StringVar()
operation_var.set(operations[0])  # Default operation
operation_menu = ttk.Combobox(root, textvariable=operation_var, values=operations, font=('calibri', 12, 'bold'))
operation_menu.grid(row=2, column=1, padx=5, pady=5)

# Buttons
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, pady=10, padx=5, sticky='ew')

clear_button = ttk.Button(root, text="Clear", command=clear_inputs)
clear_button.grid(row=3, column=2, pady=10, padx=5, sticky='ew')


# Set fixed window size
root.resizable(False, False)

# Run the main loop
root.mainloop()
