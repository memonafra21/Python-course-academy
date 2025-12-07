
# program to generate a number between 0 and 10

import random
import math 

fnum =random.random()* 10 # [0,10) --> Float
op = round(fnum)

print(op)

from random import sample

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#$%^&*(){}@"
sample_space = sample(a,10)

password = ""
for sm in sample_space:
    password += sm

print(password)