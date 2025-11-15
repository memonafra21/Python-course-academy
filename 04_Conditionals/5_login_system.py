"""
Overview
Create a simple login authentication system that validates user credentials and account verification status before granting access.
Requirements
Input
Your program should accept three inputs from the user:
- Username - A string representing the user's username
- Password - A string representing the user's password
- Verification Status - A string ("yes" or "no") indicating if the user's account is verified

Validation Rules
Implement the following validation checks in order:

1.Empty Field Check: Neither username nor password should be empty
	- If either field is empty, display: "Error: Username and password cannot be empty!"
2.Password Length Check: Password must be at least 8 characters long
	- If password is too short, display: "Error: Password must be at least 8 characters long!"
3.Admin Access: For admin users with full privileges
	- Username: "admin"
	- Password: "admin123"
	- Must be verified
	- Display: "Welcome, Admin! Full access granted."
4.Admin Without Verification: Admin credentials correct but not verified
	- Username: "admin"
	- Password: "admin123"
	- Not verified
	- Display: "Login successful, but please verify your account."
5.Regular User Access: For regular users
	- Username: "user"
	- Password: "password123"
	- Must be verified
	- Display: "Welcome, User! Access granted."
6.Invalid Credentials: Any other combination
	- Display: "Invalid credentials. Access denied."
Output
Display appropriate messages based on the validation results as specified above.
Sample Test Cases
Test Case 1 (Empty Fields)

Input:
Username: 
Password: test123
Verification: yes
 
Output:
Error: Username and password cannot be empty!

Input:
Username: john
Password: pass
Verification: yes
 
Output:
Error: Password must be at least 8 characters long!

Input:
Username: admin
Password: admin123
Verification: yes
 
Output:
Welcome, Admin! Full access granted.
"""