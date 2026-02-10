import customtkinter as ctk

#-------configuration-------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window setup
        self.title("Calculator")
        self.geometry("350x500")
        self.resizable(False, False)

        #Variables for expression

        self.expression = ""
        self.entry_text = ctk.StringVar()

        # display screen
        self.display = ctk.CTkEntry(
            self,
            textvariable=self.entry_text,
            font=("Arial", 40),
            height=80,
            justify="right",
            state="readonly"
        )

        self.display.pack(fill="x", padx=10, pady=20)

        # Button Area
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Grid layout configuration
        self.buttons_frame.columnconfigure((0, 1, 2, 3), weight=1)
        self.buttons_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        
        # Button Layout definition
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for btn_text in buttons:
            self.create_button(btn_text, row_val, col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, col):
            # determine button color based on type
            if text == "=":
                color = "#2CC985" # Green for equals
                hover = "#229966" 
            
            elif text == "C":
                color = "#FF5555" # Red for clear
                hover = "#CC0000"
            elif text in ['/', '*', '-', '+']:
                color = "#FF9900" # Orange for operators
                hover = "#CC7A00"
            else:
                color = "#3B8ED0" # Standard Blue for numbers
                hover = "#36719F"

            button = ctk.CTkButton(
                self.buttons_frame,
                text=text,
                fg_color=color,
                font=("Arial", 24, "bold"),
                hover_color=hover,
                height=70,
                command=lambda: self.on_button_click(text)
            )

            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


    def on_button_click(self, char):
            if char == "C":
                self.expression = ""
                self.entry_text.set("")

            elif char == "=":
                try:
                    result = str(eval(self.expression))
                    self.entry_text.set(result)
                    self.expression = result

                except Exception:
                    self.entry_text.set("Error")
                    self.expression = ""
            else:
                self.expression += str(char)
                self.entry_text.set(self.expression)
                
if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()