import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Login Form")
app.geometry("300x220")

def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        result.configure(text="Login Success")
    else:
        result.configure(text="Login Failed")

entry_user = ctk.CTkEntry(app, placeholder_text="Username")
entry_user.pack(pady=10)

entry_pass = ctk.CTkEntry(app, placeholder_text="Password", show="*")
entry_pass.pack(pady=10)

btn = ctk.CTkButton(app, text="Login", command=login)
btn.pack(pady=10)

result = ctk.CTkLabel(app, text="")
result.pack(pady=10)

app.mainloop()
