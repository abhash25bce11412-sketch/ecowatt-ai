import pandas as pd
from sklearn.linear_model import LinearRegression

print("Initializing EcoWatt AI...")

# 1. Load the data from our CSV file
df = pd.read_csv('data/dataset.csv')
X = df[['Temperature_C', 'AC_Hours', 'PC_Hours']]
y = df['Total_kWh']

# 2. Train the Machine Learning Model
model = LinearRegression()
model.fit(X, y)
print("Model trained successfully on historical data!\n")

# 3. Quick Prediction Test (Simulating user input)
# What if it's 30 degrees, AC runs for 5 hours, and PC runs for 4 hours?
sample_input = [[30, 5, 4]]
prediction = model.predict(sample_input)

print(f"Test Input: 30°C, 5 hours AC, 4 hours PC")
print(f"Predicted Energy Consumption: {prediction[0]:.2f} kWh")
