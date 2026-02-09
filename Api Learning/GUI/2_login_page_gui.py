import customtkinter as ctk

ctk.set_appearance_mode('system')
ctk.set_default_color_theme("green")

app = ctk.CTk()

app.geometry("600x400")
app.title("Hello World")

title = ctk.CTkLabel(app, text="Welcome to Login", font=("Arial", 24, "bold"))
title.pack(pady=20)

email_entry = ctk.CTkEntry(app, placeholder_text="Enter your email", width=200)
email_entry.pack(pady=10)

password_entry = ctk.CTkEntry(app, placeholder_text="Enter your password", width=200, show="*")
password_entry.pack(pady=10)

def get_details():
    email = email_entry.get()
    password = password_entry.get()

    if email== "admin" and password == "12345":
        status_label.configure(
            text="Login Successfull!",
            text_color="green"
        )
        print("Success")
    else:
        status_label.configure(
            text="Incorrect Id or password!!",
            text_color="red"
        )
        print("Failed")

    email_entry.delete(0, "end")
    password_entry.delete(0, "end")

btn2 = ctk.CTkButton(
    app, 
    text="click me",
    fg_color="teal", 
    hover_color="black", 
    width=120, 
    height=30,
    command=get_details
)

btn2.pack(pady=10)

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)

app.mainloop()

 