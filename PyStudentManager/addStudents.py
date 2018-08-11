students = []

def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["nameee"].title())
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

try:    
    prompt_for_students()
    print_students_titlecase()  
except Exception:
    print("unknown, general error")