import random
import time

questions = {
    "Capital of India? ": "delhi",
    "2 + 5 = ? ": "7",
    "Color of sky? ": "blue",
    "Python is a ____? (language/tool) ": "language",
    "Sun rises in which direction? ": "east"
}

# select 3 random questions
quiz = random.sample(list(questions.items()), 3)

score = 0
start = time.time()

for q, ans in quiz:
    user = input(q).lower()
    if user == ans:
        score += 1

end = time.time()
taken = round(end - start, 2)

# result based on score
if score == 3:
    print("Excellent")
elif score == 2:
    print("Good")
else:
    print("Needs Improvement")

print("Your score:", score)
print("Time taken:", taken, "seconds")