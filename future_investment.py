# Program 6

from tkinter import *
from tkinter import messagebox

window = Tk()

window.geometry("400x400")

amount_label = Label(window, text="Amount")
amount_label.grid(column=0, row=0)
amount_text = Entry(window, width=10)
amount_text.grid(column=1, row=0)
year_label = Label(window, text="Years")
year_label.grid(column=0, row=1)
year_text = Entry(window, width=10)
year_text.grid(column=1, row=1)
interent_label = Label(window, text="Annual interest rate")
interent_label.grid(column=0, row=2)
interent_text = Entry(window, width=10)
interent_text.grid(column=1, row=2)
future_value_label = Label(window, text="Future Value")
future_value_label.grid(column=0, row=3)
future_value_text = Label(window, text="")


def caluclate():
    amount = amount_text.get()
    year = year_text.get()
    rate = interent_text.get()
    if amount.isdigit() and year.isdigit():
        amount = float(amount)
        year = float(year)
        rate = float(rate)
        result = amount * (1 + rate / 1200)**(year * 12)
        future_value_label.configure(text="%.2f" % result)
    else:
        messagebox.showerror("ERROR", "ENTER VALID INPUT")


calculate_btn = Button(window, text="Calculate", command=caluclate)
calculate_btn.grid(column=0, row=4)

window.mainloop()