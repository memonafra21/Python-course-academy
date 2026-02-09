import customtkinter as ctk

def add():
    a = entry1.get()
    b = entry2.get()
    sum = int(a) + int(b)
    label.configure(text=sum)

ctk.set_appearance_mode("system")

app = ctk.CTk()
app.title("Two Number Adder")
app.geometry("300x220")

entry1 = ctk.CTkEntry(app)
entry1.pack(pady=10)

entry2 = ctk.CTkEntry(app)
entry2.pack(pady=10)

button = ctk.CTkButton(app, text="Add", command=add)
button.pack(pady=10)

label = ctk.CTkLabel(app, text="")
label.pack(pady=10)

app.mainloop()
