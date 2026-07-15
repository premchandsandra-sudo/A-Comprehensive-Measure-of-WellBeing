# A Comprehensive Measure of Well-Being: HDI Predictor

An interactive, machine-learning-powered web application designed to predict the **Human Development Index (HDI)** of countries based on key socio-economic development indicators.

---

## 🚀 Project Overview

The Human Development Index (HDI) is a summary measure of average achievement in key dimensions of human development: a long and healthy life, being knowledgeable, and having a decent standard of living.

This project trains a **Linear Regression model** (achieving an **R² score of ~0.98**) using historical United Nations data to predict a country's HDI score. The model is integrated into a modern, responsive **Flask web application** that allows stakeholders and policy analysts to input custom parameters and instantly simulate human development scores and levels.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Install Dependencies
Install the required packages using pip:
```bash
pip install flask pandas scikit-learn joblib reportlab
```

### 3. Train the Machine Learning Model
Before launching the web app, run the model training script. This script loads `hdi.csv`, cleans the data, trains the model, outputs the R² evaluation score, and saves the trained weights to `model.pkl`:
```bash
python "5. Project Development Phase/train_model.py"
```

### 4. Launch the Web Application
Start the Flask web application locally:
```bash
python "5. Project Development Phase/app.py"
```
After running the command, open your web browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📈 Development Categories & Scale

HDI predictions are mapped to development tiers as defined by the United Nations:

| HDI Score Range | Human Development Category |
| :--- | :--- |
| **Below 0.550** | Low Human Development |
| **0.550 – 0.699** | Medium Human Development |
| **0.700 – 0.799** | High Human Development |
| **0.800 and above** | Very High Human Development |
