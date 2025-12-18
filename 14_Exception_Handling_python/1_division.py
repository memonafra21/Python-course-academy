try:
    # Accept two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform division
    result = num1 / num2
    print("Result:", result)

# Handle division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handle invalid input
except ValueError:
    print("Error: Please enter a valid number!")
