import tkinter as tk

# Function to update the expression in the entry box
def press(key):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_expression + str(key))

# Function to evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Evaluate the mathematical expression
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Create the Entry widget to display the expression
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Create buttons for numbers and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create a button for clearing the entry
clear_button = tk.Button(root, text="Clear", font=("Arial", 16), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew", ipadx=10, ipady=10)

# Add number and operation buttons to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 16), command=lambda t=text: press(t) if t != "=" else calculate())
    button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

# Make the grid rows and columns expand equally
for r in range(6):
    root.grid_rowconfigure(r, weight=1)
for c in range(4):
    root.grid_columnconfigure(c, weight=1)

# Start the Tkinter event loop
root.mainloop()
