from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("200x200")

number1_label = Label(window, text="First number")
number2_label = Label(window, text="Second number")
number_text1 = Entry(window, width=10)
number_text2 = Entry(window, width=10)

number1_label.grid(column=0, row=0)
number2_label.grid(column=0, row=1)
number_text1.grid(column=1, row=0)
number_text2.grid(column=1, row=1)


def addnum():
    num1 = number_text1.get()
    num2 = number_text2.get()
    try:
        if num1 == "" or num2 == "":
            messagebox.showerror("Error", "Enter both the numbers")
            return
        num1 = int(num1)
        num2 = int(num2)
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return
    messagebox.showinfo("Result", num1 + num2)


def subnum():
    num1 = number_text1.get()
    num2 = number_text2.get()
    try:
        if num1 == "" or num2 == "":
            messagebox.showerror("Error", "Enter both the numbers")
            return
        num1 = int(num1)
        num2 = int(num2)
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return
    messagebox.showinfo("Result", num1 - num2)


def multinum():
    num1 = number_text1.get()
    num2 = number_text2.get()
    try:
        if num1 == "" or num2 == "":
            messagebox.showerror("Error", "Enter both the numbers")
            return
        num1 = int(num1)
        num2 = int(num2)
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return
    messagebox.showinfo("Result", num1 * num2)


def divnum():
    num1 = number_text1.get()
    num2 = number_text2.get()
    res = 0
    try:
        if num1 == "" or num2 == "":
            messagebox.showerror("Error", "Enter both the numbers")
            return
        num1 = int(num1)
        num2 = int(num2)
        res = num1 / num2
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return
    messagebox.showinfo("Result", res)


add = Button(window, command=addnum, text="Add")
sub = Button(window, command=subnum, text="Sub")
div = Button(window, command=divnum, text="Div")
multi = Button(window, command=multinum, text="Multi")

add.grid(row=2, column=0)
sub.grid(row=3, column=0)
multi.grid(row=4, column=0)
div.grid(row=5, column=0)

window.mainloop()