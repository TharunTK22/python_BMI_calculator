def calculate_bmi(weight_kg, height_m):
    """Calculates BMI from weight in kg and height in meters."""
    # Formula: weight (kg) / (height (m))^2
    return round(weight_kg / (height_m ** 2), 2)

def get_bmi_category(bmi):
    """
    Classifies the BMI value into a health category.
    Returns the category as a string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else: # bmi >= 30
        return "Obese"

def main():
    """Main function to run the BMI calculator."""
    print("--- BMI Calculator ---")

    # --- Get User Input with Validation ---
    while True:
        try:
            # Prompt the user for their weight
            weight_kg = float(input("Enter your weight in kilograms (e.g., 70): "))
            if weight_kg > 0:
                break
            else:
                print("Weight must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number for weight.")

    while True:
        try:
            # Prompt the user for their height
            height_m = float(input("Enter your height in meters (e.g., 1.75): "))
            if height_m > 0:
                break
            else:
                print("Height must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number for height.")

    # --- Calculation and Output ---
    # Calculate the BMI using the collected data
    bmi_result = calculate_bmi(weight_kg, height_m)
    
    # Get the corresponding health category
    category = get_bmi_category(bmi_result)

    # Display the results to the user
    print("\n--- Your Results ---")
    print(f"Your BMI is: {bmi_result}")
    print(f"This is considered: {category}")
    
    input("\nPress Enter to exit.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()