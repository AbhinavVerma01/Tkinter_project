from tkinter import *
from tkinter import messagebox, filedialog

# Functions
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    task_list.delete(0, END)

def save_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            tasks = task_list.get(0, END)
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        task_list.delete(0, END)
        with open(file_path, "r") as file:
            for task in file.readlines():
                task_list.insert(END, task.strip())

# Main Window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")

# Frame for Task Entry
task_frame = Frame(root)
task_frame.pack(pady=10)

task_entry = Entry(task_frame, width=40)
task_entry.pack(side=LEFT, padx=5)

add_button = Button(task_frame, text="Add", command=add_task)
add_button.pack(side=RIGHT)

# Task List
task_list = Listbox(root, width=50, height=15)
task_list.pack(pady=10)

# Buttons Frame
button_frame = Frame(root)
button_frame.pack()

delete_button = Button(button_frame, text="Delete", command=delete_task)
delete_button.grid(row=0, column=0, padx=5)

clear_button = Button(button_frame, text="Clear All", command=clear_tasks)
clear_button.grid(row=0, column=1, padx=5)

save_button = Button(button_frame, text="Save", command=save_tasks)
save_button.grid(row=0, column=2, padx=5)

load_button = Button(button_frame, text="Load", command=load_tasks)
load_button.grid(row=0, column=3, padx=5)

# Run the Tkinter event loop
root.mainloop()
