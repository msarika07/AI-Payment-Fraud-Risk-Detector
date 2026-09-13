\# 🛡️ AI Risk Manager



\## AI-Powered Payment Fraud Risk Detector



An AI-based payment fraud detection system designed to help identify potentially risky transactions before they cause financial loss.



The system analyzes transaction details such as amount, location, transaction time, and transaction frequency. A Random Forest machine learning model then predicts the transaction risk and provides a risk percentage along with the major risk factors.



\---



\## 🎯 Problem Statement



Online payment systems can face financial losses because of fraudulent transactions.



The goal of this project is to build a defense-only AI system that can:



\- Detect potentially fraudulent transactions

\- Assign a risk percentage

\- Classify transactions as Low, Medium, or High risk

\- Explain the major risk factors

\- Help a reviewer decide whether a transaction needs further review



\---



\## 💡 Solution



The project uses a Random Forest machine learning model trained on a synthetic transaction dataset.



The model analyzes:



1\. Transaction amount

2\. Transaction location

3\. Transaction time

4\. Number of transactions



The prediction is returned through a Flask API and displayed on a web interface.



\---



\## ✨ Features



\- 🤖 Machine learning-based fraud detection

\- 📊 Risk percentage from the ML model

\- 🚦 Smart risk meter

\- 🔴 High / 🟠 Medium / 🟢 Low risk classification

\- 🔎 AI risk factors

\- 🌐 Web-based interface

\- ⚡ Real-time prediction through Flask API

\- 📈 Precision, Recall and F1 evaluation



\---



\## 🧠 Machine Learning Model



\### Algorithm



Random Forest Classifier



\### Model Configuration



\- Number of trees: 200

\- Maximum depth: 8

\- Class weight: Balanced

\- Random state: 42



\---



\## 📊 Dataset



The project uses a synthetic dataset containing 1,000 transaction records.



Features:



| Feature | Description |

|---|---|

| amount | Transaction amount |

| location | Transaction location |

| time | Transaction time |

| transactions | Number of transactions |

| is\_fraud | Fraud label |



The dataset is synthetic and is used for demonstration and model development. It does not contain real customer or payment information.



\---



\## 📈 Model Evaluation



The dataset was divided into:



\- 80% training data

\- 20% testing data



Current test results:



\- Accuracy: \*\*86.5%\*\*

\- Precision: \*\*86.89%\*\*

\- Recall: \*\*73.61%\*\*

\- F1 Score: \*\*79.70%\*\*



Confusion Matrix:



```text

\[\[120   8]

&#x20;\[ 19  53]]


## 🔄 How It Works

User enters transaction details
            ↓
Web Interface
            ↓
Flask API
            ↓
Random Forest ML Model
            ↓
Risk Prediction
            ↓
Risk Percentage + Risk Factors
            ↓
Risk Dashboard

## 🏗️ Architecture

👤 USER
   ↓
🌐 WEB INTERFACE
HTML + CSS + JavaScript
   ↓
⚡ FLASK API
app.py
   ↓
🤖 RANDOM FOREST MODEL
fraud_model.pkl
   ↓
🚦 RISK SCORE + RISK FACTORS
   ↓
LOW / MEDIUM / HIGH

## 🛠️ Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Flask
- Scikit-learn
- Random Forest
- CSV Dataset

## ▶️ How to Run

1. Install Python and the required libraries.
2. Generate the dataset using `generate_dataset.py`.
3. Train the Random Forest model using `train_model.py`.
4. Start the Flask server using `py app.py`.
5. Open `index.html` in a browser.
6. Enter transaction details and click **Analyze Risk**.

## 🚀 Future Improvements

- Use real-world anonymized transaction datasets.
- Add more transaction behavior features.
- Improve fraud detection accuracy.
- Add real-time transaction monitoring.
- Add an alert system for high-risk transactions.
