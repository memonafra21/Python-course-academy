

marks = int(input("enter your marks: "))
grade_range = marks // 10
grade = ""
match grade_range:
    case 10 | 9:
        grade = "A"
    case 8: 
        grade = "B"
    case 7:
        grade = "C"
    case 6: 
        grade = "D"
    case _:
        grade = "F"

if grade == "F":
    print("you have failed the exam")
else:
    print(f"your grade is {grade}")