students = open("./marks.txt", "r")
keys = open("./keys.txt", "r")

answer = []

for i in keys:
    answer = i.split()[1:]
    # there is only single line in keys
    # we split that line and asign it to answer line ignoring the first word 'key'

marks = {}  # for keeping track of each student mark

for student in students:

    # splitting each line into array
    student = student.split()

    # to get the first field in student file's each line example: 'student1'
    key = student[0]

    #creating an entry for each student
    marks[key] = 0

    #ignoring the first field to focus on options ticked by student
    student = student[1:]

    i = 0  # counter to keep track of student index
    for option in answer:
        if option == student[i]:
            # if correct option matches the one ticked by student increment the entry in the dictionary
            marks[key] += 1

        i += 1

print(marks)

students.close()
keys.close()
