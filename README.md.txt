Advanced Graphical BMI Calculator
A user-friendly desktop application built with Python to calculate Body Mass Index (BMI), track historical data, and visualize health trends over time.

Objective
The primary goal of this project is to provide a comprehensive and intuitive tool for users to monitor their BMI. It moves beyond a simple calculation by offering features for data persistence and historical analysis, empowering users to track their health journey effectively.

Key Features & Steps Performed
Graphical User Interface (GUI):

Developed a clean and intuitive interface using Python's built-in Tkinter library.

The UI provides clear input fields for weight and height, a prominent calculation button, and a dedicated area to display the results.

BMI Calculation & Categorization:

Implemented the standard BMI formula: weight (kg) / (height (m))^2.

The application automatically classifies the calculated BMI into one of four standard health categories: Underweight, Normal weight, Overweight, or Obese.

The result is color-coded for immediate visual feedback.

Data Storage:

User entries (weight, height, BMI, and date) are automatically saved to a local CSV file (bmi_data.csv).

The pandas library is used to manage the data, making it robust and easy to handle. This ensures that a user's history is preserved between sessions.

Historical Data Visualization:

A "View History" feature generates a dynamic graph showing the user's BMI trend over time.

This visualization is created using the matplotlib library and is embedded directly within a new application window.

The graph includes shaded regions corresponding to the different health categories, making it easy to see how the user's BMI has changed relative to health benchmarks.

User Input Validation & Error Handling:

The application includes checks to ensure that users enter valid, positive numbers for weight and height, preventing crashes from incorrect input.

Graceful error messages are displayed for file I/O issues or other unexpected problems.

Tools & Technologies Used
Programming Language: Python 3

GUI Library: Tkinter (Python's standard GUI package)

Data Manipulation: pandas (For creating and appending to the CSV data file)

Data Visualization: matplotlib (For plotting the historical BMI graph)

Project Outcome
The final result is a standalone, functional desktop application that serves as a personal health tool. It successfully calculates BMI, provides immediate feedback, and, most importantly, stores and visualizes historical data. This allows users not just to see a single data point, but to understand the broader trends in their health, making it a much more powerful and useful tool than a simple one-off calculator.

How to Run the Project
Clone the repository or download the files.

Install the necessary dependencies:

pip install -r requirements.txt

Run the application from your terminal:

python bmi_calculator.py


Create a README.md file: This is the welcome page for your project. It's written in Markdown. Create a file named README.md and add something like this:

# Advanced BMI Calculator

A user-friendly graphical BMI calculator built with Python and Tkinter.

## Features

-   Calculate BMI from weight (kg) and height (cm).
-   Classify BMI into health categories (Underweight, Normal, Overweight, Obese).
-   Save historical data to a local CSV file.
-   Visualize your BMI trend over time with a graph.

## How to Run

1.  Clone the repository.
2.  Install the dependencies: `pip install -r requirements.txt`
3.  Run the script: `python bmi_calculator.py`
