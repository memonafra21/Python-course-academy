# Input a number
num = int(input("Enter a number: "))

rev = 0   # to store reversed number

# Use loop to reverse the digits
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

# Print the reversed number
print("Reversed number:", rev)
