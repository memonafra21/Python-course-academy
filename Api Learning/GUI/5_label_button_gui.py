import customtkinter as ctk

# Create main window
app = ctk.CTk()
app.title("My First GUI")
app.geometry("300x200")

# Create Label
label = ctk.CTkLabel(app, text="My First GUI App")
label.pack(pady=10)

# Create Button
button = ctk.CTkButton(app, text="Click Me")
button.pack(pady=10)

# Display window
app.mainloop()
