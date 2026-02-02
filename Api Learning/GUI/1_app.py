import customtkinter as ctk

def on_click():
    print("Button was clicked!!!")

# Step 1: create main window
app = ctk.CTk()

# Step 2: Set window size

app.geometry("400x400")

# step 3: set app title

app.title("My First GUI")

# step 4: start GUI loop

label = ctk.CTkLabel(app, text="Hello world!")
label.pack(pady=20)

button = ctk.CTkButton(app, text="click me",command=on_click )
button.pack()

app.mainloop()