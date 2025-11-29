# Input an email address
email = input("Enter your email address: ")  # e.g., "student123@gmail.com"

# Slice out the username (everything before '@')
username = email.split('@')[0]

# Remove the first and last character from the username
trimmed_username = username[1:-1]

# Print both the original username and the trimmed username
print("Original username:", username)
print("Trimmed username:", trimmed_username)
