import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


data = pd.read_csv('sme_data.csv')


X = data[['SME_Age', 'Annual_Revenue_Category', 'Liquidity_Stability', 'Risk_Awareness']]
y = data['Financial_Distress']


model = RandomForestClassifier(random_state=42)
model.fit(X, y)


joblib.dump(model, 'model.pkl')

print("Model Training Completed Successfully and model.pkl created!")