import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter import colorchooser, filedialog
import os

# Create the application window
application_window = tk.Tk()

messagebox.showinfo("Information","Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")

rgb_color, web_color = colorchooser.askcolor(parent=application_window,
                                             initialcolor=(255, 0, 0))

answer = messagebox.askokcancel("Question","Do you want to open this file?")
print(answer)
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
print(answer)
answer = messagebox.askyesno("Question","Do you like Python?")
print(answer)
answer = messagebox.askyesnocancel("Question", "Continue playing?")
print(answer)

answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=application_window)
if answer is not None:
    print("Your first name is ", answer)
else:
    print("You don't have a first name?")

answer = simpledialog.askinteger("Input", "What is your age?",
                                 parent=application_window,
                                 minvalue=0, maxvalue=100)
if answer is not None:
    print("Your age is ", answer)
else:
    print("You don't have an age?")

answer = simpledialog.askfloat("Input", "What is your salary?",
                               parent=application_window,
                               minvalue=0.0, maxvalue=100000.0)
if answer is not None:
    print("Your salary is ", answer)
else:
    print("You don't have a salary?")

# Build a list of tuples for each file type the file dialog should display
my_filetypes = [('all files', '.*'), ('text files', '.txt')]

# Ask the user to select a folder.
answer = filedialog.askdirectory(parent=application_window,
                                 initialdir=os.getcwd(),
                                 title="Please select a folder:")
print(answer)
# Ask the user to select a single file name.
answer = filedialog.askopenfilename(parent=application_window,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)
print(answer)
# Ask the user to select a one or more file names.
answer = filedialog.askopenfilenames(parent=application_window,
                                     initialdir=os.getcwd(),
                                     title="Please select one or more files:",
                                     filetypes=my_filetypes)
print(answer)
# Ask the user to select a single file name for saving.
answer = filedialog.asksaveasfilename(parent=application_window,
                                      initialdir=os.getcwd(),
                                      title="Please select a file name for saving:",
                                      filetypes=my_filetypes)
print(answer)

# Create the user interface
my_label = ttk.Label(application_window, text="Hello World!")
my_label.grid(row=2, column=1)

# Start the GUI event loop
application_window.mainloop()