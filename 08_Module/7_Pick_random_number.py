import random

# Computer picks a random number between 1 and 10
number = random.choice([1,2,3,4,5,6,7,8,9,10])

# User enters a guess
guess = int(input("Enter your guess (1 to 10): "))

# Check result
if guess == number:
    print("Correct guess!")
else:
    print("Wrong guess! The correct number was:", number)
