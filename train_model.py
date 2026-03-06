import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import joblib

# -----------------------------
# LOAD YOUR DATASET
# -----------------------------
data = pd.read_csv("traindata.csv")

print("Columns in dataset:", data.columns)

# Rename columns for easy usage
data.rename(columns={
    'LV ActivePower (kW)': 'ActivePower',
    'Wind Speed (m/s)': 'WindSpeed',
    'Theoretical_Power_Curve (KWh)': 'TheoreticalPower'
}, inplace=True)

# -----------------------------
# HANDLE MISSING VALUES
# -----------------------------
data.dropna(inplace=True)

# -----------------------------
# VISUALIZATION
# -----------------------------
sns.scatterplot(x=data["WindSpeed"], y=data["ActivePower"])
plt.title("Wind Speed vs Active Power")
plt.show()

# -----------------------------
# SELECT FEATURES & TARGET
# -----------------------------
X = data[["WindSpeed", "TheoreticalPower"]]
y = data["ActivePower"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = RandomForestRegressor(n_estimators=50, random_state=42)

model.fit(X_train, y_train)

# -----------------------------
# EVALUATE MODEL
# -----------------------------
preds = model.predict(X_test)

print("R2 Score:", r2_score(y_test, preds))
print("RMSE:", np.sqrt(mean_squared_error(y_test, preds)))

# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, "power_prediction.pkl")
print("Model saved as power_prediction.pkl")
