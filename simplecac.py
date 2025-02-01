import tkinter as tk

# Function to perform calculations
def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result.set("Cannot divide by zero")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create StringVar for displaying the result
result = tk.StringVar()

# Create the input fields
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1)

# Create the operation buttons
btn_add = tk.Button(root, text="+", width=10, command=add)
btn_add.grid(row=1, column=0)

btn_subtract = tk.Button(root, text="-", width=10, command=subtract)
btn_subtract.grid(row=1, column=1)

btn_multiply = tk.Button(root, text="*", width=10, command=multiply)
btn_multiply.grid(row=2, column=0)

btn_divide = tk.Button(root, text="/", width=10, command=divide)
btn_divide.grid(row=2, column=1)

# Create a label to display the result
result_label = tk.Label(root, textvariable=result, width=10)
result_label.grid(row=3, column=0, columnspan=2)

# Run the application
root.mainloop()
