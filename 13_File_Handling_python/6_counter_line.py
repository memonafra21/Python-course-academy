# Take 3 lines of text from the user and store in data.txt
with open("data.txt", "w") as f:
    for i in range(3):
        line = input(f"Enter line {i+1}: ")
        f.write(line + "\n")

# Read the file and count the number of lines
with open("data.txt", "r") as f:
    lines = f.readlines()

# Display number of lines
print("Number of lines in the file:", len(lines))