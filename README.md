# ⚡ EcoWatt AI - Smart Energy Consumption Forecaster

### 🎯 Project Overview
EcoWatt AI is a machine learning-based command-line tool developed in Python. It addresses the real-world problem of unpredictable electricity bills and energy waste by predicting a household's daily energy consumption (in kWh) based on weather conditions and appliance usage.

### 📉 Problem Statement
People often struggle to understand how their daily habits impact their electricity consumption until the monthly bill arrives. This "energy blindness" leads to wasted power and higher costs. 

### 💡 Solution
EcoWatt AI provides a simple, predictive solution that:
* Uses **Multiple Linear Regression** to understand the relationship between daily variables and energy use.
* Takes simple user inputs (average temperature, hours the AC was on, number of active laptops).
* Instantly predicts the total energy consumed for the day to help users make informed decisions.

### 💻 Technology Stack
* **Python 3.x** - Core programming language
* **scikit-learn** - For building and training the Machine Learning model
* **pandas** - For data manipulation and reading datasets

### 🚀 How to Run the Project
1. **Clone the repository:**
   `git clone https://github.com/YOUR_USERNAME/ecowatt-ai.git`
2. **Install dependencies:**
   `pip install pandas scikit-learn`
3. **Run the AI model:**
   `python main.py`
