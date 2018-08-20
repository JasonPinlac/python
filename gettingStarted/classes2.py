students = []

class Student:
    def __init__(self, name="John Doe", student_id=0, student_grades=[]):
        self.name = name
        self.student_id = student_id
        self.student_grades = student_grades

    def __str__(self):
        return f"Student object:\n\tname:{self.name},\n\tstudent_id:{self.student_id},\n\tstudent_grades:{self.student_grades}"

student1 = Student()
student2 = Student("Jason Pinlac", 1, [99, 98, 100, 103])


students.append(student1)
students.append(student2)


print(students)

for student in students:
    print(student)
