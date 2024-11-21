import tkinter as tk
from tkinter import messagebox

# Function to display a message
def show_message():
    messagebox.showinfo("Hello", "Welcome to Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")  # Set the size of the window

# Create a button and attach the show_message function
button = tk.Button(root, text="Click Me!", command=show_message)
button.pack(pady=20)  # Add some vertical padding

# Start the Tkinter event loop
root.mainloop()
#trying to work 