# Input principal, rate, and time
principal = int(input("Enter principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))

# Calculate simple interest
interest = (principal * rate * time) / 100

# Print the interest
print("Simple Interest =", interest)
