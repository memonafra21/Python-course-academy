import customtkinter as ctk
# Create main window
app = ctk.CTk()
app.title("Simple Form")
app.geometry("300x200")

# Label for Name
label = ctk.CTkLabel(app, text="Enter Name:")
label.pack(pady=5)

entry = ctk.CTkEntry(app)

entry.pack(pady=5)

# Submit Button
button = ctk.CTkButton(app, text="Submit")
button.pack(pady=10)
app.mainloop()
