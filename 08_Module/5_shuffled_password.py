import random

sample_space = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#$%^&*(){}@")

random.shuffle(sample_space)

shuffled = "".join(sample_space)
print(f"The password is {shuffled[0:12]}")