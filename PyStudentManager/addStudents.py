students = []

def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def prompt_for_students():
    while(True):
        name = input("Enter a student name: ")
        student_id = input("Enter a student id: ")
        add_student(name, student_id)
        response = input("Would you like to enter another student (y/n): ")
        if(response == "n"):
            break

def read_file():
    f = open("students.txt", "r")
    for student in f.readlines():
        student_details = student.split(",")
        print(student_details)
        if len(student_details) > 1:
            add_student(student_details[0], student_details[1].strip('\n'))
    f.close()

def save_file():
    f = open("students.txt", "w") # a is an access mode. There is r, a, w and more
    for student in students:
        f.write("{0},{1}\n".format(student["name"], student["student_id"]))
    f.close()

# try:
read_file()
print(students)
prompt_for_students()
save_file()
# except Exception as error:
#     print("Error: {0}".format(error))
