# Take 5 numbers from the user and store in a list
numbers = []      # empty list

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Print the list
print("\nNumbers entered:", numbers)

# Calculate sum
total = sum(numbers)

# Calculate average
average = total / len(numbers)

# Print sum and average
print("Sum of numbers:", total)
print("Average of numbers:", average)
