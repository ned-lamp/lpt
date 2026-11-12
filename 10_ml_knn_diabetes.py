"""
10 - K-Nearest Neighbors on Diabetes Dataset

Aim: Implement K-Nearest Neighbors algorithm on diabetes.csv dataset. Compute
     confusion matrix, accuracy, error rate, precision and recall.

Dataset: diabetes.csv -> https://www.kaggle.com/datasets/abdallamahgoub/diabetes
         (768 patients, 8 features, Outcome: 1 = Diabetic, 0 = Not diabetic)

Complexity:
  Training   : O(1)         -> only stores the data
  Prediction : O(n x f)     -> distance to all n training points with f features
  Space      : O(n x f)     -> keeps the whole training set

Key terms:
  KNN                : finds K nearest points and takes a majority vote.
  Euclidean distance : sqrt((x1-x2)^2 + (y1-y2)^2 + ...)
  K                  : number of neighbours; small K = noisy, large K = too smooth; use odd K.
  Non-parametric     : makes no assumption about the shape of the data.
  Scaling            : must do, else big-number columns (Insulin) dominate distance.
  Confusion matrix   : table of TN, FP, FN, TP.
  Accuracy   = (TP + TN) / Total
  Error rate = (FP + FN) / Total = 1 - Accuracy
  Precision  = TP / (TP + FP)
  Recall     = TP / (TP + FN)   -> most important in medical cases (missing a patient is bad)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# 1. Load data
df = pd.read_csv("diabetes.csv")
X = df.drop(columns=["Outcome"])
y = df["Outcome"]                       # 1 = Diabetic, 0 = Not diabetic

# 2. Split and scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 3. Train KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

# 4. Evaluate
cm = confusion_matrix(y_test, pred)
acc = accuracy_score(y_test, pred)

print("Confusion Matrix:\n", cm)
print("Accuracy   :", acc)
print("Error Rate :", 1 - acc)
print("Precision  :", precision_score(y_test, pred))
print("Recall     :", recall_score(y_test, pred))
