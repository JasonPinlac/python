
class Student:
    # static attribute
    school_name = "Jupiter Elementary"

    # constructor
    def __init__(self, name, student_id="0"):
        # instance attributes
        self.name = name
        self.student_id = student_id
    # overridden __str__ method that is output on print()
    def __str__(self):
        return f"Student object:\n\tname: {self.name}\n\tstudent_id: {self.student_id}\n\t{self.school_name}"

    # instance methods
    def get_name_capitalized(self):
        return self.name.capitalize()
    
    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):

    def __str__(self):
        return f"HighSchoolStudent object:\n\tname: {self.name}\n\tstudent_id: {self.student_id}\n\t{self.school_name}"

    def get_school_name(self):
        org_val = super().get_school_name()
        return org_val + "-HS"
        
student1 = Student("Jason", 1)
student2 = HighSchoolStudent("Mike", 2)

# print(student1)
# print(student2)

print(student1.get_school_name())
print(student2.get_school_name())