"""
19 - Bank Customer Churn Prediction (Neural Network)
(EXTRA: ML Assignment 3 of the syllabus - missing from the lab manual)

Aim: Given a bank customer, build a neural network-based classifier that can
     determine whether they will leave or not in the next 6 months.
     Read dataset, separate features and target, normalize, build the model,
     print accuracy and confusion matrix.

Dataset: Churn_Modelling.csv -> https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling
         (Exited: 1 = left the bank, 0 = stayed)

Complexity:
  Training   : O(e x n x w) -> e epochs, n rows, w = number of weights in network
  Prediction : O(w) per customer
  Space      : O(w)         -> stores the weights

Key terms:
  Churn            : a customer leaving the bank/service.
  ANN              : Artificial Neural Network = input layer + hidden layers + output layer.
  Neuron           : computes weighted sum of inputs + bias, then applies an activation.
  Activation       : ReLU in hidden layers, sigmoid/logistic at output (gives probability).
  Backpropagation  : sends the error backwards to update weights (uses gradient descent).
  Epoch            : one full pass over the training data (max_iter here).
  get_dummies      : converts text columns (Geography, Gender) into 0/1 numbers.
  Normalization    : scaling features to same range so training is stable.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load and separate features / target
df = pd.read_csv("Churn_Modelling.csv")
df = df.drop(columns=["RowNumber", "CustomerId", "Surname"])
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)

X = df.drop(columns=["Exited"])
y = df["Exited"]

# 2. Split and normalize
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 3. Build and train neural network (2 hidden layers of 6 neurons)
model = MLPClassifier(hidden_layer_sizes=(6, 6), max_iter=500, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluate
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
