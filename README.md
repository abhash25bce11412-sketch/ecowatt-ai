# ⚡ EcoWatt AI – Smarter Energy Monitoring System

## 📌 Problem Statement

In shared environments like hostels, PGs, and apartments, electricity usage is not tracked individually. This leads to unfair billing and excessive energy consumption, as users are unaware of their real-time usage.

A system is needed to provide clear visibility and intelligent insights into energy consumption.

---

## 💡 Solution Overview

EcoWatt AI is an AI-based system that monitors electricity usage and represents it in a **battery percentage format**, making it simple and easy to understand.

The system uses machine learning to:

* Predict future electricity consumption
* Detect abnormal usage patterns
* Provide alerts to users

---

## 🚀 Features

* 🔋 Energy usage in battery percentage
* 📊 Real-time tracking
* 🤖 AI-based prediction
* ⚠️ Anomaly detection
* 📈 Visualization dashboard

---

## 🛠️ Tech Stack

* Frontend: Streamlit
* Backend: FastAPI
* Language: Python
* Libraries: Pandas, NumPy, Scikit-learn

---

## 🏗️ Project Structure

```
ecowatt-ai/
│
├── app.py              # Streamlit frontend
├── main.py             # FastAPI backend
├── model.py            # ML model logic
├── dataset.csv         # Data used for training/testing
└── requirements.txt
```

---

## 📊 Dataset

* Contains historical electricity usage data
* Includes time-based consumption values
* Used for training the prediction model

---

## 🤖 Model Used

* Type: Time Series Forecasting
* Input: Past energy usage data
* Output: Predicted future consumption

---

## 🔌 API Endpoints

* `/predict` → Returns predicted energy usage
* `/data` → Returns current usage data

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/abhash25bce11412-sketch/ecowatt-ai.git
cd ecowatt-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run backend:

```
uvicorn main:app --reload
```

Run frontend:

```
streamlit run app.py
```

---

## 📊 Output

* Dashboard showing energy usage
* Battery percentage representation
* Prediction graphs
* Alerts for abnormal usage

*(Add screenshots here for better presentation)*

---

## 🧠 Learnings

* Applied machine learning to a real-world problem
* Learned time series prediction
* Worked with FastAPI and Streamlit

---

## ⚠️ Challenges

* Data preprocessing for accurate predictions
* Integrating ML model with frontend
* Maintaining prediction accuracy

---

## 🔮 Future Scope

* IoT-based real-time data collection
* Mobile application development
* Improved prediction models

---


## 📜 Note

This project reflects continuous learning and development.
Output
<img width="1718" height="95" alt="Screenshot 2026-03-28 022845" src="https://github.com/user-attachments/assets/23aa51d6-d748-43ce-91ef-dc79dfc45b78" />

👨‍💻 Author

 Name:Abhash Pandey
 Registration No-25BCE11412
Course: Fundamentals of AI and ML 

