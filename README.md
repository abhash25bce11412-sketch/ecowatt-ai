# ⚡ EcoWatt AI - Smart Energy Consumption Forecaster

⚡ EcoWatt AI – Smarter Energy Monitoring System
📌 Problem Statement

In shared environments like hostels, PGs, and apartments, electricity usage is often not tracked individually. This leads to unfair billing and excessive energy consumption, as users are unaware of their real-time usage.

There is a need for a system that provides clear visibility and intelligent insights into energy consumption.

💡 Solution Overview

EcoWatt AI is an AI-based system that monitors electricity usage and represents it in a battery percentage format, making it easy to understand.

The system uses machine learning to:

Predict future energy consumption
Detect unusual usage patterns
Provide alerts to users
🚀 Features
🔋 Energy usage in battery percentage
📊 Real-time tracking
🤖 AI-based prediction
⚠️ Anomaly detection
📈 Visualization dashboard
🛠️ Tech Stack
Frontend: Streamlit
Backend: FastAPI
Language: Python
Libraries: Pandas, NumPy, Scikit-learn
🏗️ Project Architecture
ecowatt-ai/
│
├── frontend/
├── backend/
├── models/
├── data/
├── utils/
├── app.py
├── main.py
└── requirements.txt
⚙️ Installation

Clone the repository:

git clone https://github.com/abhash25bce11412-sketch/ecowatt-ai.git
cd ecowatt-ai

Install dependencies:

pip install -r requirements.txt
▶️ Usage

Run backend:

uvicorn main:app --reload

Run frontend:

streamlit run app.py
📊 Output
Dashboard showing energy usage
Battery percentage representation
Prediction graphs
<img width="1718" height="95" alt="Screenshot 2026-03-28 022845" src="https://github.com/user-attachments/assets/23aa51d6-d748-43ce-91ef-dc79dfc45b78" />

🧠 Learnings
Applied machine learning to a real-world problem
Learned time series prediction
Worked with FastAPI and Streamlit
⚠️ Challenges
Handling data for prediction
Integrating ML model with UI
Maintaining accuracy
🔮 Future Scope
IoT-based real-time data collection
Mobile application
Improved prediction models
📜 Note
This repository reflects continuous development and learning.

👨‍💻 Author

 Name:Abhash Pandey
 Registration No-25BCE11412
Course: Fundamentals of AI and ML 

