import customtkinter as ctk

# Create main window
app= ctk.CTk()
app.title("Temperature convertor")
app.geometry("400x300")


# Function to convert Celsius to Fahrenheit
def convert_temp():
    try:
        celsius = float(temp_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.configure(text=f"Result: {fahrenheit:.2f} °F")
    except ValueError:
        result_label.configure(text="Error: Please enter a valid number")

# Header Label
header_label = ctk.CTkLabel(
    app,
    text="Temperature Converter",
    font=("Arial", 20, "bold")
)
header_label.grid(row=0, column=0, columnspan=2, pady=20)

# Input Label
temp_label = ctk.CTkLabel(
    app,
    text="Enter Temperature (°C):"
)
temp_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

# Input Entry
temp_entry = ctk.CTkEntry(
    app,
    placeholder_text="e.g., 25"
)
temp_entry.grid(row=1, column=1, padx=20, pady=10)

# Convert Button
convert_button = ctk.CTkButton(
    app,
    text="Convert to Fahrenheit",
    command=convert_temp
)
convert_button.grid(row=2, column=0, columnspan=2, pady=20)

# Output Label
result_label = ctk.CTkLabel(
    app,
    text="Result:"
)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the app
app.mainloop()