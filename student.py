from tkinter import *
import pymysql
from tkinter import messagebox

db = pymysql.connect(host='localhost',
                     user='root',
                     password='*******',
                     db='empdb')

curser = db.cursor()

curser.execute("DROP TABLE IF EXISTS STUDENT")

curser.execute("""
  CREATE TABLE STUDENT(
    USN VARCHAR(10),
    NAME VARCHAR(20),
    AGE INTEGER,
    BRANCH VARCHAR(15)
  )
""")

window = Tk()

window.geometry("300x300")
usn_label = Label(window, text="USN")
usn_label.grid(column=0, row=0)
usn_text = Entry(window, width=10)
usn_text.grid(column=1, row=0)
name_label = Label(window, text="NAME")
name_label.grid(column=0, row=1)
name_text = Entry(window, width=10)
name_text.grid(column=1, row=1)
age_label = Label(window, text="AGE")
age_label.grid(column=0, row=2)
age_text = Entry(window, width=10)
age_text.grid(column=1, row=2)
branch_label = Label(window, text="BRANCH")
branch_label.grid(column=0, row=3)
branch_text = Entry(window, width=10)
branch_text.grid(column=1, row=3)


def insert():
    usn = usn_text.get()
    name = name_text.get()
    age = age_text.get()
    branch = branch_text.get()
    if len(usn) != 0 and len(name) != 0 and len(age) != 0 and len(branch) != 0:
        try:
            curser.execute(
                f"INSERT INTO STUDENT VALUES({usn},'{name}',{age},'{branch}')")
            db.commit()
            messagebox.showinfo("Insert", "INSERTION SUCCESSFUL")
        except:
            db.rollback()
            messagebox.showinfo("error", "INSERTION FAILED")
    else:
        messagebox.showinfo("PLEASE ENTER ALL THE FIELDS")


def search():
    usn = usn_text.get()
    if len(usn) != 0:
        try:
            curser.execute(f"SELECT * FROM STUDENT WHERE USN={usn}")
            if (curser.rowcount != 0):
                row = curser.fetchone()
                messagebox.showinfo(
                    "Insert",
                    f"USN : {row[0]}\nNAME : {row[1]}\nAGE : {row[2]}\nBRANCH : {row[3]}"
                )
            else:
                messagebox.showinfo("error", "THERE IS NO SUCH RECORD")
        except:
            messagebox.showinfo("error", "INSERTION FAILED")
    else:
        messagebox.showinfo("PLEASE ENTER USN")


insert = Button(window, text="INSERT STUDENT", command=insert)
insert.grid(column=0, row=4)
search = Button(window, text="SEARCH BY USN", command=search)
search.grid(column=1, row=4)
window.mainloop()
