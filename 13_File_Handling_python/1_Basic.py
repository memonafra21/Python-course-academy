f = open("message.txt", "w")

while True:
    msg = input("Please give me a message: ")
    
    if msg.lower() == "stop":
        break
    
    f.write(msg + '\n')

f.close()

print("Message saved successfully!")
