try:
    file = open("example2.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()