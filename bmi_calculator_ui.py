import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    """Calculates BMI and displays the result."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0 or weight <= 0:
            messagebox.showwarning("Input Error", "Weight and height must be positive numbers.")
            return

        # BMI calculation formula: weight (kg) / (height (m))^2
        # Assuming height is in cm, convert to meters
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        result_label.config(text=f"Your BMI is: {bmi:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the main application window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
# Weight input
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Height input
height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Result display
result_label = tk.Label(root, text="Your BMI is: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()