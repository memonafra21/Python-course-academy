import customtkinter as ctk     
from tkinter import messagebox

# --------- App Settings ---------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"


class LoginApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Login System")
        self.geometry("400x300")

        self.create_login_window()

    # ---------------- LOGIN WINDOW ----------------
    def create_login_window(self):

        self.clear_window()

        self.label_title = ctk.CTkLabel(self, text="Login", font=("Arial", 24))
        self.label_title.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.validate_login)
        self.login_button.pack(pady=20)

    # ---------------- VALIDATION ----------------
    def validate_login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            self.create_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    # ---------------- DASHBOARD ----------------
    def create_dashboard(self, username):

        self.clear_window()

        welcome_label = ctk.CTkLabel(self, text=f"Welcome, {username}", font=("Arial", 20))
        welcome_label.pack(pady=40)

        logout_button = ctk.CTkButton(self, text="Logout", command=self.create_login_window)
        logout_button.pack(pady=20)

    # ---------------- CLEAR WINDOW ----------------
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()


# Run App
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()


