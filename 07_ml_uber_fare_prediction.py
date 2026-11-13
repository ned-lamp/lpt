"""
07 - Uber Ride Price Prediction (Linear Regression vs Random Forest)

Aim: Predict the price of the Uber ride from a given pickup point to the agreed
     drop-off location.
     1. Pre-process the dataset  2. Identify outliers  3. Check the correlation
     4. Implement linear regression and random forest regression models
     5. Evaluate the models and compare their scores like R2, RMSE

Dataset: uber.csv -> https://www.kaggle.com/datasets/yasserh/uber-fares-dataset

Complexity:
  Linear Regression : O(n x f^2)          (n = rows, f = features)
  Random Forest     : O(t x n log n x f)  (t = number of trees)

Key terms:
  Regression        : predicting a number (here: fare amount).
  Linear Regression : fits a straight line between features and target.
  Random Forest     : many decision trees, final answer = average of all trees.
  Outlier           : a value far away from normal values (fare 0, 5000 km trip).
  IQR               : Q3 - Q1; values outside Q1-1.5*IQR .. Q3+1.5*IQR are outliers.
  Correlation       : how strongly two columns move together (-1 to +1).
  Haversine         : formula for distance between two lat/long points on Earth.
  R2 score          : how much of the fare variation the model explains (closer to 1 = better).
  RMSE              : average size of prediction error (lower = better).

Formulas:  (y = actual, y^ = predicted, y_bar = mean)
  Correlation (r) = sum((x - x_bar)(y - y_bar)) / sqrt( sum((x - x_bar)^2) * sum((y - y_bar)^2) )
                    +1 = rise together, -1 = one rises other falls, 0 = no relation
  Linear Reg.     : y^ = b0 + b1*x1 + b2*x2 + ...   (b = coefficients learned from data)
  Random Forest   : y^ = average of predictions of all trees
                    (each tree trained on a random sample of rows/features -> less overfitting)
  R2              = 1 - sum((y - y^)^2) / sum((y - y_bar)^2)     (1 = perfect, 0 = just guessing mean)
  RMSE            = sqrt( (1/n) * sum((y - y^)^2) )              (same unit as fare)
  IQR             = Q3 - Q1 ; outlier if value < Q1 - 1.5*IQR or > Q3 + 1.5*IQR
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# 1. Load and pre-process
df = pd.read_csv("uber.csv")
df = df.drop(columns=["Unnamed: 0", "key"])
df = df.dropna()

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.dayofweek
df = df.drop(columns=["pickup_datetime"])

# Distance in km from coordinates (Haversine formula)
lat1, lon1 = np.radians(df["pickup_latitude"]), np.radians(df["pickup_longitude"])
lat2, lon2 = np.radians(df["dropoff_latitude"]), np.radians(df["dropoff_longitude"])
a = np.sin((lat2 - lat1) / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2
df["distance"] = 6371 * 2 * np.arcsin(np.sqrt(a))

# 2. Remove outliers (IQR method)
for col in ["fare_amount", "distance"]:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]
df = df[(df["fare_amount"] > 0) & (df["distance"] > 0)]

# 3. Correlation
print("Correlation with fare:\n", df.corr()["fare_amount"])

# 4. Train models
X = df[["distance", "passenger_count", "hour", "day"]]
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression().fit(X_train, y_train)
rf = RandomForestRegressor(n_estimators=50, random_state=42).fit(X_train, y_train)

# 5. Evaluate and compare
for name, model in [("Linear Regression", lr), ("Random Forest", rf)]:
    pred = model.predict(X_test)
    print(name)
    print("  R2   :", r2_score(y_test, pred))
    print("  RMSE :", np.sqrt(mean_squared_error(y_test, pred)))
