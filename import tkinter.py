import tkinter
from tkinter import *

# Initialize the main application window
root = Tk()
root.title("Simple Calculator")  # Set the title of the window
root.geometry("570x600+100+200")  # Set the size and position of the window
root.resizable(False, False)  # Disable resizing of the window
root.configure(bg="#17161b")  # Set the background color of the window

# Global variable to hold the equation as a string
equation = ""

def show(value):
    """Append a value to the equation and update the display.

    Args:
        value (str): The value to be appended to the equation.
    """
    global equation
    equation += value  # Append the value to the equation
    label_result.config(text=equation)  # Update the display label

def clear():
    """Clear the equation and reset the display."""
    global equation
    equation = ""  # Reset the equation
    label_result.config(text=equation)  # Update the display label

def delete():
    """Delete the last character from the equation."""
    global equation
    equation = equation[:-1]  # Remove the last character
    label_result.config(text=equation)  # Update the display label

def calculate():
    """Evaluate the equation and display the result."""
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)  # Evaluate the equation
        except:
            result = "error"  # Display error for invalid input
            equation = ""  # Reset the equation
    label_result.config(text=result)  # Update the display label

# Label to display the equation or result
label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# Button layout and functionality
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=clear).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("/")).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3687f5", command=lambda: show("%")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3687f5", command=lambda: show("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("-")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: show("+")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)
Button(root, text="Del", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=delete).place(x=290, y=500)

Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=calculate).place(x=430, y=400)

# Run the application
root.mainloop()

   

