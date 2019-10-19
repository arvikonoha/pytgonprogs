import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='*********',
                     db='empdb')

curser = db.cursor()

curser.execute("DROP TABLE IF EXISTS EMPLOYEE")

curser.execute("""
  CREATE TABLE EMPLOYEE(
    SSN INTEGER,
    FIRST_NAME VARCHAR(20),
    LAST_NAME VARCHAR(20),
    AGE INTEGER,
    PLACE VARCHAR(15),
    SALARY INTEGER
  )
""")

while True:
    choice = input("Enter your choice (insert,delete,update)")
    if (choice == "insert"):
        print("Enter your details")
        ssn = input("SSN : ")
        first_name = input("First name : ")
        last_name = input("Last name : ")
        age = input("Age : ")
        place = input("Place : ")
        salary = input("Salary : ")
        try:
            curser.execute(
                f"INSERT INTO EMPLOYEE VALUES({ssn},'{first_name}','{last_name}',{age},'{place}',{salary})"
            )
            db.commit()
            print("INSERTION SUCCESSFUL")
        except:
            print("ERROR INSERTING RECORD")
            db.rollback()
    elif (choice == "delete"):
        print("Enter the ssn of the row to be deleted")
        ssn = input("SSN : ")
        try:
            curser.execute(f"DELETE FROM EMPLOYEE WHERE SSN={ssn}")
            db.commit()
            if (curser.rowcount == 0):
                print("THERE IS NO SUCH RECORD")
            else:
                print(curser.rowcount, " ROWS DELETED")
        except:
            print("ERROR DELETING RECORD")
    elif (choice == "update"):
        print("Enter the ssn of the row to be deleted")
        ssn = input("SSN : ")
        print("Enter your details to update")
        first_name = input("First name : ")
        last_name = input("Last name : ")
        age = input("Age : ")
        place = input("Place : ")
        salary = input("Salary : ")
        try:
            curser.execute(
                f"UPDATE EMPLOYEE SET FIRST_NAME='{first_name}',LAST_NAME='{last_name}',AGE={age},PLACE='{place}',SALARY={salary} WHERE SSN={ssn}"
            )
            db.commit()
            if (curser.rowcount == 0):
                print("THERE IS NO SUCH RECORD")
            else:
                print(curser.rowcount, " ROWS UPDATED")
        except:
            print("ERROR UPDATING RECORDS")
            db.rollback()
    else:
        print("BYE")
        break
