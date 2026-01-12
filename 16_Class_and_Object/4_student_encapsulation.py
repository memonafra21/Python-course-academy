# Student Information System using OOP
# Concepts: Encapsulation, Getter & Setter, Public & Protected Variables

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name            # public variable
        self._roll_no = roll_no     # protected variable
        self.__marks = marks        # private variable

    # Public method
    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self._roll_no)

    # Getter for private variable __marks
    @property
    def marks(self):
        return self.__marks

    # Setter for private variable __marks
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks! Marks should be between 0 and 100.")



# Object Creation (Outside class)

student1 = Student("Afra", 101, 85)

# Using public method
student1.display_info()

# Using getter to access private variable
print("Marks:", student1.marks)

# Using setter to update private variable
student1.marks = 92
print("Updated Marks:", student1.marks)


student1.marks = 150
