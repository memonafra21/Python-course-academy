try:
    # Accept a number from the user
    num = int(input("Enter a number: "))
    
    # Check even or odd
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Handle invalid input
except ValueError:
    print("Error: Please enter a valid integer!")
