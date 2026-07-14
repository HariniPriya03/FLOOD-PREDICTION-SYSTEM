# Rising Waters – Flood Prediction Using Machine Learning
### AI AND ML PROJECT

## Project Overview

Rising Waters is a Machine Learning-based Flood Prediction System that predicts whether flood conditions are likely to occur based on historical weather parameters. The application helps users analyze flood risk using a trained XGBoost model integrated into a Flask web application.

The project uses historical weather data obtained from Kaggle and provides an easy-to-use web interface where users can enter weather-related parameters to receive instant flood predictions.

---

## Objectives

- Predict flood occurrence using Machine Learning.
- Compare multiple machine learning algorithms.
- Select the best-performing model.
- Deploy the trained model using Flask.
- Provide an easy-to-use web application for prediction.

---

## Features

- Historical flood prediction using Machine Learning
- Data preprocessing using StandardScaler
- Comparison of multiple ML algorithms:
  - Decision Tree
  - Random Forest
  - K-Nearest Neighbors (KNN)
  - XGBoost
- XGBoost selected as the final model
- Flask-based web application
- Simple and responsive user interface
- Instant Flood / No Flood prediction

---

## Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- XGBoost

### Backend
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Libraries
- Pandas
- NumPy
- Joblib
- Matplotlib
- Seaborn

### Development Tools
- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

## Project Structure

```
Flood_Prediction_System/
│
├── app.py
├── Flood_Prediction.ipynb
├── floods.save
├── transform.save
├── requirements.txt
├── README.md
├── dataset.xlsx
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── chance.html
│   └── no_chance.html
│
├── static/
│   ├── main.css
│   ├── main.js
│   └── flood.jpg
│
└── Project Documentation/
```

---

## Dataset

**Source:** Kaggle

### Input Features

- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall

### Target Variable

- Flood

---

## Machine Learning Workflow

1. Dataset Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Feature Scaling
6. Model Training
7. Model Evaluation
8. Model Selection
9. Model Saving
10. Flask Deployment

---

## Machine Learning Models Used

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

After evaluation using Accuracy Score, Confusion Matrix, and Classification Report, **XGBoost** achieved the highest performance and was selected as the final prediction model.

---

## Installation

### Clone the repository

```bash
git clone <your-github-repository-link>
```

---

### Navigate to the project folder

```bash
cd Flood_Prediction_System
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run the application

```bash
python app.py
```

---

### Open your browser

```
http://127.0.0.1:5000/
```

---

## How to Use

1. Open the application.
2. Click **Predict**.
3. Enter:
   - Cloud Cover
   - Annual Rainfall
   - Jan-Feb Rainfall
   - Mar-May Rainfall
   - Jun-Sep Rainfall
4. Click **Predict Flood**.
5. View the prediction result.

---

## Application Pages

- Home Page
<img width="1907" height="911" alt="Screenshot 2026-07-13 165720" src="https://github.com/user-attachments/assets/9ee56df1-5485-4728-bb01-0d97ae19a629" />

- Prediction Page
<img width="1907" height="907" alt="Screenshot 2026-07-13 165751" src="https://github.com/user-attachments/assets/6cc58cf4-f021-4528-9d89-4efea2ca4af7" />

- Flood Result Page
<img width="1897" height="908" alt="Screenshot 2026-07-13 165936" src="https://github.com/user-attachments/assets/4fc2b76d-d061-4ca6-b3da-b60c85356c1e" />

- No Flood Result Page
<img width="1911" height="915" alt="Screenshot 2026-07-13 170047" src="https://github.com/user-attachments/assets/1eb0efee-df24-48e7-b973-9af6ecbdfed6" />


---

## Model Evaluation

The models were evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

The **XGBoost** classifier achieved the best overall performance and was selected for deployment.

---

## Future Enhancements

- Real-time Weather API integration
- Cloud deployment (Render / AWS / Azure)
- User Authentication
- SMS & Email Alerts
- GIS-based Flood Mapping
- Mobile Application
- Larger Training Dataset

---

## Developed By

**Harini Priya Gurrala**

B.Tech – Computer Science and Data Science

SmartBridge Internship Project

---

## 📄 License

This project is developed for educational and internship purposes.
