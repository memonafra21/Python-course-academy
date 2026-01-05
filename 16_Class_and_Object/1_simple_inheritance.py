# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)


# Child class
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)   # calling parent constructor
        self.roll_number = roll_number

    def student_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)


# Creating object of Student
student1 = Student("Afra", 20, 21)

# Calling methods
student1.greet()
student1.student_info()
