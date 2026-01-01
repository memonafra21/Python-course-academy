score = 0

print("Quiz Game Start\n")

# Question 1
print("1. What is the capital of India?")
print("a) Mumbai  b) Delhi  c) Chennai")
ans = input("Enter your answer: ")
if ans == "b":
    score += 1

# Question 2
print("\n2. Which keyword is used to define a function in Python?")
print("a) func  b) def  c) function")
ans = input("Enter your answer: ")
if ans == "b":
    score += 1

# Question 3
print("\n3. What is 10 + 5?")
print("a) 10  b) 15  c) 20")
ans = input("Enter your answer: ")
if ans == "b":
    score += 1

print("\nYour final score is:", score)