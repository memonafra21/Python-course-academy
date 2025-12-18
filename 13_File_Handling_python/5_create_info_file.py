# Create a file named info.txt and write name & city
with open("info.txt", "w") as f:
    f.write("Name: Afra\n")
    f.write("City: Ahmedabad\n")

# Read and display the file content
with open("info.txt", "r") as f:
    content = f.read()


print(content)
