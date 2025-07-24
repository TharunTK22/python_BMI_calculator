import tkinter as tk
from tkinter import messagebox
import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Constants ---
DATA_FILE = 'bmi_data.csv'
CATEGORIES = {
    "Underweight": (0, 18.5),
    "Normal weight": (18.5, 24.9),
    "Overweight": (25, 29.9),
    "Obese": (30, float('inf'))
}
BG_COLOR = "#f0f8ff"  # Alice Blue
BUTTON_COLOR = "#4682b4" # Steel Blue
TEXT_COLOR = "#2f4f4f" # Dark Slate Gray
FONT_NORMAL = ("Helvetica", 12)
FONT_BOLD = ("Helvetica", 14, "bold")
FONT_TITLE = ("Helvetica", 18, "bold")


class BMICalculatorApp(tk.Tk):
    """
    An advanced BMI Calculator with a graphical user interface,
    data storage, and historical trend visualization.
    """
    def __init__(self):
        super().__init__()
        self.title("Advanced BMI Calculator")
        self.geometry("500x600")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        
        # Initialize data file if it doesn't exist
        self.init_data_file()

        # Create and pack widgets
        self.create_widgets()

    def init_data_file(self):
        """Creates the CSV data file with headers if it doesn't exist."""
        if not os.path.exists(DATA_FILE):
            try:
                # Create a pandas DataFrame with the required columns
                df = pd.DataFrame(columns=['date', 'weight_kg', 'height_cm', 'bmi'])
                # Save it to a CSV file
                df.to_csv(DATA_FILE, index=False)
            except IOError as e:
                messagebox.showerror("File Error", f"Could not create data file: {e}")
                self.destroy()

    def create_widgets(self):
        """Creates and lays out all the GUI elements."""
        main_frame = tk.Frame(self, bg=BG_COLOR, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # --- Title ---
        title_label = tk.Label(main_frame, text="BMI Calculator", font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR)
        title_label.pack(pady=(0, 20))

        # --- Input Frame ---
        input_frame = tk.Frame(main_frame, bg=BG_COLOR)
        input_frame.pack(pady=10)

        # Weight input
        tk.Label(input_frame, text="Weight (kg):", font=FONT_NORMAL, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.weight_entry = tk.Entry(input_frame, font=FONT_NORMAL, width=15)
        self.weight_entry.grid(row=0, column=1, padx=5, pady=5)

        # Height input
        tk.Label(input_frame, text="Height (cm):", font=FONT_NORMAL, bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.height_entry = tk.Entry(input_frame, font=FONT_NORMAL, width=15)
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)

        # --- Buttons Frame ---
        button_frame = tk.Frame(main_frame, bg=BG_COLOR)
        button_frame.pack(pady=20)
        
        calc_button = tk.Button(button_frame, text="Calculate BMI", font=FONT_BOLD, bg=BUTTON_COLOR, fg="white", command=self.calculate_and_display)
        calc_button.grid(row=0, column=0, padx=10)

        history_button = tk.Button(button_frame, text="View History", font=FONT_BOLD, bg=BUTTON_COLOR, fg="white", command=self.show_history)
        history_button.grid(row=0, column=1, padx=10)
        
        # --- Result Display ---
        self.result_label = tk.Label(main_frame, text="", font=FONT_BOLD, bg=BG_COLOR, fg=TEXT_COLOR)
        self.result_label.pack(pady=10)
        
        self.category_label = tk.Label(main_frame, text="", font=FONT_NORMAL, bg=BG_COLOR, fg=TEXT_COLOR)
        self.category_label.pack()

    def calculate_and_display(self):
        """
        Handles the entire process of calculation, categorization,
        saving data, and updating the display.
        """
        try:
            weight_kg = float(self.weight_entry.get())
            height_cm = float(self.height_entry.get())

            if weight_kg <= 0 or height_cm <= 0:
                messagebox.showwarning("Input Error", "Weight and height must be positive values.")
                return

            # BMI Calculation: weight (kg) / (height (m))^2
            height_m = height_cm / 100
            bmi = round(weight_kg / (height_m ** 2), 2)
            
            # Categorization
            category = self.get_bmi_category(bmi)

            # Display results
            self.result_label.config(text=f"Your BMI: {bmi}")
            self.category_label.config(text=f"Category: {category}", fg=self.get_category_color(category))

            # Save data
            self.save_data(weight_kg, height_cm, bmi)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def get_bmi_category(self, bmi):
        """Classifies the BMI value into a health category."""
        for category, (min_val, max_val) in CATEGORIES.items():
            if min_val <= bmi < max_val:
                return category
        return "Unknown"

    def get_category_color(self, category):
        """Returns a color based on the BMI category for visual feedback."""
        if category == "Underweight":
            return "blue"
        elif category == "Normal weight":
            return "green"
        elif category == "Overweight":
            return "orange"
        elif category == "Obese":
            return "red"
        return TEXT_COLOR

    def save_data(self, weight, height, bmi):
        """Appends the new BMI record to the CSV file."""
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_data = pd.DataFrame([[now, weight, height, bmi]], columns=['date', 'weight_kg', 'height_cm', 'bmi'])
            # Append to the CSV file without writing headers
            new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
        except IOError as e:
            messagebox.showerror("File Error", f"Could not save data: {e}")

    def show_history(self):
        """Displays a new window with a graph of historical BMI data."""
        try:
            if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) < 50: # Check if file has more than just headers
                messagebox.showinfo("No Data", "No historical data to display yet. Calculate your BMI first!")
                return
            
            df = pd.read_csv(DATA_FILE)
            if df.empty:
                messagebox.showinfo("No Data", "No historical data to display yet. Calculate your BMI first!")
                return
            
            # --- Create the history window ---
            history_win = tk.Toplevel(self)
            history_win.title("BMI History")
            history_win.geometry("700x500")
            history_win.configure(bg=BG_COLOR)

            # --- Create the plot ---
            fig, ax = plt.subplots(figsize=(7, 5))
            df['date'] = pd.to_datetime(df['date']) # Convert date string to datetime objects
            ax.plot(df['date'], df['bmi'], marker='o', linestyle='-', color=BUTTON_COLOR)
            
            # Add horizontal lines for categories
            ax.axhspan(CATEGORIES["Underweight"][0], CATEGORIES["Underweight"][1], color='lightblue', alpha=0.3, label='Underweight')
            ax.axhspan(CATEGORIES["Normal weight"][0], CATEGORIES["Normal weight"][1], color='lightgreen', alpha=0.3, label='Normal')
            ax.axhspan(CATEGORIES["Overweight"][0], CATEGORIES["Overweight"][1], color='moccasin', alpha=0.3, label='Overweight')
            ax.axhspan(CATEGORIES["Obese"][0], max(40, df['bmi'].max()+2), color='lightcoral', alpha=0.3, label='Obese')

            # Formatting
            ax.set_title("BMI Trend Over Time", fontdict={'fontsize': 16, 'fontweight': 'bold'})
            ax.set_xlabel("Date", fontdict={'fontsize': 12})
            ax.set_ylabel("BMI", fontdict={'fontsize': 12})
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            fig.autofmt_xdate() # Auto-rotate date labels
            ax.legend()
            
            # --- Embed plot in Tkinter window ---
            canvas = FigureCanvasTkAgg(fig, master=history_win)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
        except FileNotFoundError:
            messagebox.showinfo("No Data", "The data file was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not display history: {e}")


if __name__ == "__main__":
    app = BMICalculatorApp()
    app.mainloop()
