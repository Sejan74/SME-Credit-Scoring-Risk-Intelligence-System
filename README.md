# SME-Credit-Scoring-Risk-Intelligence-System
# 🛡️ SME Credit Scoring & Risk Intelligence System

An interactive machine learning application designed to evaluate small and medium enterprise (SME) creditworthiness, assess financial distress, and automate loan approval decisions.

---

## 📌 Project Overview
Evaluating SME credit risk is a critical challenge for financial institutions due to unstructured financial records and varying risk profiles. This project leverages Machine Learning to predict **Financial Distress (Loan Default Risk)** using key business indicators such as operational age, revenue scale, liquidity stability, and management risk awareness.

---

## 🎯 Key Features
* **Machine Learning Engine:** Powered by a `Random Forest Classifier` trained on real-world business financial indicators.
* **Instant Risk Scoring:** Predicts loan approval status (`Low Risk` vs. `High Risk`) in real time.
* **Interactive UI:** Built with Streamlit for a clean, responsive, and user-friendly experience.
* **Feature Integration:** Evaluates SME Age, Annual Revenue Category, Liquidity Stability, and Risk Awareness.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-Learn
* **Model Serialization:** Joblib
* **Web Framework:** Streamlit

---
## Interface Preview
![SME Credit Scoring App Interface](https://github.com/Sejan74/SME-Credit-Scoring-Risk-Intelligence-System/blob/main/screencapture-localhost-8501-2026-10-13-01_48_27.png?raw=true)
## 📂 Project Structure
```text
├── sme_data.csv.csv      # SME Financial Dataset
├── train.py              # Script to train the ML model and save model.pkl
├── model.pkl             # Trained Random Forest Model
├── app22.py              # Streamlit UI Application
                          # Project Documentation
