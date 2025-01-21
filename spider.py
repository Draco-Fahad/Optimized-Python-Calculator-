#### CODE BY FAHAD ULLAH ####
import customtkinter as ctk

# Initialize the main app
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("dark-blue")  # Options: "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("FAHADz Calculator")
app.geometry("400x600")


# MAIN FUNCTIONS
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        elif operation == "**":
            result = num1 ** num2
        else:
            result = "Invalid Operation"
        result_label.configure(text=f"Result: {result}")
    except ValueError:
        result_label.configure(text="Error: Invalid input")



def clear():
    entry_num1.delete(0, ctk.END)
    entry_num2.delete(0, ctk.END)
    result_label.configure(text="Result: ")
    operation_var.set("+")



header_frame = ctk.CTkFrame(app, corner_radius=10)
header_frame.pack(pady=10, fill="x", padx=20)

header_label = ctk.CTkLabel(
    header_frame, text="FAHADz Calculator", font=("Arial", 24, "bold")
)
header_label.pack(pady=10)


input_frame = ctk.CTkFrame(app, corner_radius=10)
input_frame.pack(pady=10, padx=20, fill="x")

entry_num1 = ctk.CTkEntry(
    input_frame, placeholder_text="Enter first number", font=("Arial", 16)
)
entry_num1.pack(pady=10, padx=10, fill="x")

entry_num2 = ctk.CTkEntry(
    input_frame, placeholder_text="Enter second number", font=("Arial", 16)
)
entry_num2.pack(pady=10, padx=10, fill="x")


operation_var = ctk.StringVar(value="+")
operation_menu = ctk.CTkOptionMenu(
    input_frame,
    values=["+", "-", "*", "/", "**"],
    variable=operation_var,
    font=("Arial", 14),
)
operation_menu.pack(pady=10, padx=10)


button_frame = ctk.CTkFrame(app, corner_radius=10)
button_frame.pack(pady=20, padx=20, fill="x")

calculate_button = ctk.CTkButton(
    button_frame, text="Calculate", command=calculate, font=("Arial", 16)
)
calculate_button.pack(side="left", padx=20, pady=10, expand=True)

clear_button = ctk.CTkButton(
    button_frame, text="Clear", command=clear, font=("Arial", 16), fg_color="red"
)
clear_button.pack(side="right", padx=20, pady=10, expand=True)


result_frame = ctk.CTkFrame(app, corner_radius=10)
result_frame.pack(pady=20, padx=20, fill="x")

result_label = ctk.CTkLabel(
    result_frame, text="Result: ", font=("Arial", 18, "bold"), anchor="w"
)
result_label.pack(pady=10, padx=10, fill="x")


footer_label = ctk.CTkLabel(
    app,
    text="Developed by FAHAD ULLAH",
    font=("Arial", 12, "italic"),
    text_color="gray",
)
footer_label.pack(pady=10)

# Run the app
app.mainloop()
