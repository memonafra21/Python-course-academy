# Input a number n
n = int(input("Enter a number: "))

# Loop to print numbers from 1 to n
print("Numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(i, end=" ")

print()  # for new line

# Loop to print numbers from n to 1 (reverse order)
print("Numbers from", n, "to 1:")
for i in range(n, 0, -1):
    print(i, end=" ")
