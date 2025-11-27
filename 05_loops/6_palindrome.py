# Input a number
num = int(input("Enter a number: "))

original = num   # store original number
rev = 0          # to store reversed number

# Reverse the number using loop
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

# Check palindrome
if original == rev:
    print("It is a Palindrome Number")
else:
    print("It is NOT a Palindrome Number")
