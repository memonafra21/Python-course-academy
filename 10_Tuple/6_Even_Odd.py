# Creating a tuple of 10 integers
numbers = (10, 15, 22, 33, 40, 55, 60, 71, 80, 95)

# Initialize counters
even_count = 0
odd_count = 0

# Loop through the tuple
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print results
print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
