class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    # # getter method of marks
    # def get_marks(self):
    #     return self._marks
    
    # getter
    @property
    def marks(self):
        return self.__marks

    #  setter
    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("invalid marks")
    

s1 = Student("Rahul", 85)

s1.marks = 96

 
# s1.get_marks()
print(s1.marks)