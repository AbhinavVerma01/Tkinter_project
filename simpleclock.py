import tkinter as tk
import time

# Function to update the time on the label
def time_update():
    current_time = time.strftime("%H:%M:%S")  # Get current time in hour:minute:second format
    label.config(text=current_time)  # Update the label text with the current time
    label.after(1000, time_update)  # Call the function every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Simple Clock")

# Set the window size
root.geometry("250x100")

# Create a label to display the time
label = tk.Label(root, font=("calibri", 40, "bold"), background="black", foreground="white")
label.pack(anchor="center")

# Call the time_update function to display and update the time
time_update()

# Run the application
root.mainloop()
