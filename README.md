🎓 Student Placement Prediction Using Machine Learning

An end-to-end machine learning project that predicts whether a student will get placed based on academic and aptitude indicators such as CGPA and IQ. This system helps students and institutions take proactive career decisions using data-driven insights.

📌 Project Overview

Student placement is a major concern in today’s competitive job market. This project uses supervised machine learning classification algorithms to analyze student performance data and predict placement outcomes.

A user-friendly Flask web application allows users to enter CGPA and IQ values and instantly receive placement predictions.

🚀 Features

Predicts placement status: Placed / Not Placed

Uses multiple ML algorithms for model comparison

Logistic Regression

Random Forest

Decision Tree

KNN

SVM

Naive Bayes

Best-performing model deployed using Flask

Clean & responsive web interface

Handles invalid inputs with user-friendly error messages

🛠️ Tech Stack
Category	Tools
Programming	Python
ML Libraries	Pandas, NumPy, Scikit-learn
Visualization	Matplotlib, Seaborn
Web Framework	Flask
Model Storage	Joblib
Frontend	HTML, CSS
Dataset	Kaggle – College Placement Dataset
📂 Project Structure
placement_prediction/
│
├── app.py
├── placement_model.pkl
├── scaler.pkl
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
│
└── static/
    └── css/
        └── style.css

⚙️ Installation & Setup
Step 1: Clone the Repository
git clone https://github.com/your-username/student-placement-prediction.git
cd student-placement-prediction

Step 2: Create Virtual Environment
python -m venv venv


Activate environment:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
python app.py


Open your browser and go to:

http://127.0.0.1:5000

📊 Example Input
CGPA	IQ	Prediction
8.2	135	Placed
5.0	70	Not Placed
📈 Learning Outcomes

Data preprocessing & feature scaling

Classification model comparison

Flask-based ML deployment

End-to-end ML project lifecycle

🔮 Future Enhancements

Add technical skills, internships, certifications

Implement Explainable AI

Mobile application version

Cloud deployment

Personalized career recommendation dashboard

🤝 Connect With Me

Surya Teja Chakkala
Aspiring Cloud & AI Engineer
