import random

names = ["Aarav", "Ishita", "Kabir", "Meera", "Rohan", "Saanvi", "Vihaan"]
classes = ["6th", "7th", "8th", "9th", "10th"]
subjects = ["Math", "Science", "English", "History", "Computer"]

student = {
    "name": random.choice(names),
    "age": random.randint(12, 18),
    "class": random.choice(classes),
    "subject": random.choice(subjects),
    "marks": random.randint(0, 100)
}

print(student)
