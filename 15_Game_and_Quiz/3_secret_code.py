import random
import time

# generate 6 digit code
code = random.randint(100000, 999999)
print("Secret code:", code)

# start timer
start = time.time()

user = input("Enter the code: ")

# stop timer
end = time.time()
taken = end - start

if user == str(code):
    print("Success! Time taken:", round(taken, 2), "seconds")
else:
    print("Try again")