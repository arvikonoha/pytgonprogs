from tkinter import *
import pymysql
from tkinter import messagebox

db = pymysql.connect(host='localhost',
                     user='root',
                     password='nevergivup99',
                     db='empdb')

curser = db.cursor()

window = Tk()

nameT = StringVar()  # newline
branchT = StringVar()  # newline
ageT = StringVar()  # newline

window.geometry("300x300")
usn_label = Label(window, text="USN")
usn_label.grid(column=0, row=0)
usn_text = Entry(window, width=10)
usn_text.grid(column=1, row=0)
name_label = Label(window, text="NAME")
name_label.grid(column=0, row=1)
name_text = Entry(window, width=10, textvariable=nameT)  # newline
name_text.grid(column=1, row=1)
age_label = Label(window, text="AGE")
age_label.grid(column=0, row=2)
age_text = Entry(window, width=10, textvariable=ageT)  # newline
age_text.grid(column=1, row=2)
branch_label = Label(window, text="BRANCH")
branch_label.grid(column=0, row=3)
branch_text = Entry(window, width=10, textvariable=branchT)  # newline
branch_text.grid(column=1, row=3)


def search():
    usn = usn_text.get()
    if len(usn) != 0:
        try:
            curser.execute(f"SELECT * FROM STUDENT WHERE USN={usn}")
            if (curser.rowcount != 0):
                row = curser.fetchone()
                messagebox.showinfo("success", "Record obtained")
                nameT.set(row[1])
                ageT.set(row[2])
                branchT.set(row[3])
            else:
                messagebox.showinfo("error", "THERE IS NO SUCH RECORD")
        except:
            messagebox.showinfo("error", "INSERTION FAILED")
    else:
        messagebox.showinfo("PLEASE ENTER USN")


search = Button(window, text="SEARCH BY USN", command=search)
search.grid(column=1, row=4)
window.mainloop()