import numpy as np
import pandas as pd
from xgboost import XGBClassifier
import pickle
from sklearn.preprocessing import LabelEncoder

# Importing model binary
with open("fraud_detection_model.pkl", "rb") as file:
    model = pickle.load(file)
print("ML Model Loaded Successfully")

# Importing encoded data
df = pd.read_csv("X_test.csv")
print("CSV Loaded Successfully")


# Using model binary to generate predictions array
predictions = model.predict(df)

print("Number of fraudulent transactions: ", sum(predictions))

id_list = []
for index, value in enumerate(predictions):
    if value == 1:  # Check if transaction is fraudulent
        id_list.append(index)  # Append the index of the fraudulent transaction        

print(id_list)

