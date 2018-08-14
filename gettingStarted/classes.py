
class Student:

    # static variables
    school_name = "Jupiter High School"

    # static methods
    def get_school():
        return "Jupiter High School"

    # consctuctor
    def __init__(self, name, student_id="0"):
        # instance attributes
        self.name = name
        self.student_id = student_id
    
    def __str__(self):
        return self.name + " " + self.student_id

    # instance methods
    def get_name_capitalized(self):
        return self.name.capitalize()

  

def add_student(student):
    students.append(student)

students = []

student1 = Student("jason", "7")


print(student1.name + student1.student_id)

print(student1.get_name_capitalized())


print(Student.get_school())
print(Student.school_name)