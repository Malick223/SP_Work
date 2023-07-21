class Student:
    # __init__ method is a method that automatically
    # Gets called everytime objects are created
    # self represents the object calling it

    def check_pass_fail(self):
        if self.marks >= 40:
            return True

        else:
            return False


    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# Values "Harry" and 85 passed to name and marks automatically
student1 = Student("Harry", 85)
student2 = Student("Janet", 30)
print(student1.name)
print(student1.marks)
print(student2.name)
print(student2.marks)

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)

""" def check_pass_fail(self):
        if self.marks >= 40:
            return True

        else:
            return False

# Objects of student class, attributes name and marks added
student1 = Student()
student1.name = "Harry"
student1.marks = 85

# Returning result from function check_pass_fail
did_pass = student1.check_pass_fail()

print(did_pass)

student2 = Student()
student2.name = "Janet"
student2.marks = 30
did_pass = student2.check_pass_fail()
print(did_pass)
"""