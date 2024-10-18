import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import tkinter as tk
from tkinter import messagebox

# Step 1: Generate synthetic data
np.random.seed(42)
house_size = np.random.rand(100, 1) * 1000  # House sizes between 0 to 1000 square feet
house_price = house_size * 300 + np.random.randn(100, 1) * 10000  # Random noise added

# Create DataFrame
data = pd.DataFrame({
    'Size': house_size.flatten(),
    'Price': house_price.flatten()
})

# Split the data into training and testing sets
X = data[['Size']]
y = data['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Create the GUI using Tkinter
def predict_price():
    try:
        size = float(entry_size.get())
        # Predict price using a 2D array for input, as required by scikit-learn
        prediction = model.predict([[size]])  # Use double brackets for a 2D array
        # Extract the scalar from the NumPy array and format it
        label_result.config(text=f"Predicted Price: ${prediction[0]:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the house size.")



def plot_data():
    # Plot the dataset
    plt.scatter(X, y, color='blue', label='Actual Data')
    plt.plot(X_test, model.predict(X_test), color='red', label='Predicted Prices')
    plt.xlabel("Size of House (Square Feet)")
    plt.ylabel("Price of House (USD)")
    plt.title("House Size vs Price")
    plt.legend()
    plt.show()

# Initialize Tkinter window
root = tk.Tk()
root.title("House Price Predictor")
root.geometry("400x300")

# Create labels and text entry for house size
label_title = tk.Label(root, text="Predict House Price", font=("Arial", 16))
label_title.pack(pady=10)

label_size = tk.Label(root, text="Enter House Size (in square feet):", font=("Arial", 12))
label_size.pack()

entry_size = tk.Entry(root, font=("Arial", 12))
entry_size.pack(pady=5)

# Create a button to predict price
button_predict = tk.Button(root, text="Predict Price", command=predict_price, font=("Arial", 12))
button_predict.pack(pady=10)

# Label to display the result
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

# Create a button to plot data
button_plot = tk.Button(root, text="Plot Data", command=plot_data, font=("Arial", 12))
button_plot.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
