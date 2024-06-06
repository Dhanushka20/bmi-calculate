import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        # Define bold font
        bold_font = tkfont.Font(weight="bold")

        # Labels and entry fields for height and weight with bold font
        self.weight_label = tk.Label(root, text="Weight (kg):", font=bold_font)
        self.weight_label.pack(pady=5)
        self.weight_entry = tk.Entry(root, font=bold_font)
        self.weight_entry.pack(pady=5)

        self.height_label = tk.Label(root, text="Height (cm):", font=bold_font)
        self.height_label.pack(pady=5)
        self.height_entry = tk.Entry(root, font=bold_font)
        self.height_entry.pack(pady=5)

        # Calculate button with custom colors and bold font
        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi, fg='white', bg='blue', font=bold_font)
        self.calculate_button.pack(pady=10)

        # Label to display the result with bold font
        self.result_label = tk.Label(root, text="", font=bold_font)
        self.result_label.pack(pady=5)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height_cm = float(self.height_entry.get())
            height_m = height_cm / 100  # Convert height to meters

            bmi = weight / (height_m ** 2)
            self.result_label.config(text=f"BMI: {bmi:.2f}")
            self.display_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

    def display_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        self.result_label.config(text=f"BMI: {bmi:.2f} ({category})")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
