# Write a program to generate random 12 character password

import random

sample_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#$%^&*(){}@"

password = ""

for i in range (1,13):
    random_ch = random.choice(sample_space)
    password += random_ch

print(f"The password is: {password}")