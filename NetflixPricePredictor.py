import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
import numpy as np

# Load your pre-trained model
model = joblib.load("C:\\Users\\aneesh\\Desktop\\Internship\\netflix\\lr11.pkl")

def make_prediction(input_data):
    try:
        prediction = model.predict([input_data])[0]
        return prediction
    except Exception as e:
        # Handle any exceptions that might occur during prediction
        raise

def format_prediction(prediction):
    return f"{prediction:.2f}"

def predict():
    try:
        # Get input data from the form
        input_data = {
            'Open': float(entry_open.get()),
            'High': float(entry_high.get()),
            'Low': float(entry_low.get()),
            'Volume': float(entry_volume.get())
        }

        # Make predictions using your model
        prediction = make_prediction(list(input_data.values()))

        # Format the prediction
        formatted_prediction = format_prediction(prediction)

        # Display the formatted prediction in the label
        prediction_label.config(text=f"Predicted Close Value: {formatted_prediction}")

    except ValueError as ve:
        # Handle ValueError (e.g., if the conversion to float fails)
        messagebox.showerror("Error", f"Invalid input: {str(ve)}")

    except Exception as e:
        # Handle other exceptions
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Stock Price Predictor")
root.geometry("500x400")  # Set a larger window size
root.configure(bg='#ADD8E6')  # Set background color

# Create and place labels and entry fields
label_open = ttk.Label(root, text="Open:")
entry_open = ttk.Entry(root)
label_high = ttk.Label(root, text="High:")
entry_high = ttk.Entry(root)
label_low = ttk.Label(root, text="Low:")
entry_low = ttk.Entry(root)
label_volume = ttk.Label(root, text="Volume:")
entry_volume = ttk.Entry(root)

# Center the input fields
center_frame = ttk.Frame(root, style='TFrame', padding=(10, 5, 10, 5), relief="solid", borderwidth=1)
center_frame.grid(row=5, column=0, columnspan=2, pady=20)

label_open.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
entry_open.grid(row=0, column=1, padx=5, pady=5)
label_high.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
entry_high.grid(row=1, column=1, padx=5, pady=5)
label_low.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
entry_low.grid(row=2, column=1, padx=5, pady=5)
label_volume.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
entry_volume.grid(row=3, column=1, padx=5, pady=5)

# Create a style for the button
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))
# Create and place the "Predict" button with larger font
predict_button = ttk.Button(root, text="Predict", command=predict, style='TButton')
predict_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create a label to display the prediction with larger font
prediction_label = ttk.Label(root, text="", font=('Arial', 14))
prediction_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
