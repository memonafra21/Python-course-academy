# Input a number
num = int(input("Enter a number: "))

# Store original number for display (optional)
temp = num

sum_digits = 0
product_digits = 1

# Use loop to extract digits
while num > 0:
    digit = num % 10       # extract last digit
    sum_digits += digit    # add to sum
    product_digits *= digit  # multiply for product
    num = num // 10        # remove last digit

# Print values
print("Sum of digits =", sum_digits)
print("Product of digits =", product_digits)
