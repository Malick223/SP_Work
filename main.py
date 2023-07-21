class Person:
    # Object
    #use the __init() function to assign values for name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # The __str__() function controls what should be returned
    # when the class object is represented as a string
    """def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
print(p1)"""

    # Methods in objects are functions that belong to the object
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
