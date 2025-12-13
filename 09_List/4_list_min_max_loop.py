# Create a list of 10 numbers
numbers = [12, 5, 78, 23, 9, 34, 56, 1, 67, 45]

# Initialize largest and smallest with the first element
largest = numbers[0]
smallest = numbers[0]

# Loop through the list
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Print the results
print("Numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
