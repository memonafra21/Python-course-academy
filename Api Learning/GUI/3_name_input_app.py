import customtkinter as ctk

def say_hello():
    name = entry.get()
    label.configure(text="Hello " + name)

# appearance
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

# main window
app = ctk.CTk()
app.title("Name Input App")
app.geometry("300x200")

# entry box
entry = ctk.CTkEntry(app, placeholder_text="Enter your name")
entry.pack(pady=20)

# button
button = ctk.CTkButton(app, text="Click Me", command=say_hello)
button.pack(pady=10)

# label
label = ctk.CTkLabel(app, text="")
label.pack(pady=10)

app.mainloop()
