"""
08 - Email Spam Detection (KNN and SVM)

Aim: Classify the email using the binary classification method. Email Spam
     detection has two states: a) Normal State - Not Spam, b) Abnormal State - Spam.
     Use K-Nearest Neighbors and Support Vector Machine and analyze their performance.

Dataset: emails.csv -> https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv
         (each column = a word, value = its count; Prediction: 1 = Spam, 0 = Not Spam)

Complexity:
  KNN : training O(1) (just stores data), prediction O(n x f) per email
  SVM : training about O(n^2) to O(n^3), prediction fast

Key terms:
  Binary classification : only 2 output classes (Spam / Not Spam).
  KNN                   : looks at K nearest emails and takes a majority vote.
  Lazy learner          : KNN does no training, all work happens at prediction time.
  SVM                   : finds the best line (hyperplane) separating the 2 classes.
  Margin                : gap between the hyperplane and nearest points; SVM maximizes it.
  Support vectors       : the points closest to the boundary.
  Kernel                : how SVM draws the boundary (linear, rbf, poly).
  Scaling               : brings all columns to same range (needed for distance-based models).
  Accuracy  = (TP + TN) / Total
  Precision = TP / (TP + FP)   -> of predicted spam, how many are really spam
  Recall    = TP / (TP + FN)   -> of real spam, how many were caught
  F1 score  = 2 * Precision * Recall / (Precision + Recall)

Formulas:
  KNN distance (Euclidean) = sqrt((x1 - x2)^2 + (y1 - y2)^2 + ...)
  KNN steps : choose K -> find distance to all training emails -> take K nearest
              -> majority vote = class
  SVM hyperplane : w . x + b = 0      (w = weights, b = bias)
  SVM margin     = 2 / ||w||          (SVM maximizes this gap)
  SVM decision   : w . x + b >= 0 -> Spam, else Not Spam

KNN vs SVM:
  KNN : simple, no training, slow prediction, sensitive to scaling and K.
  SVM : slower training, fast prediction, usually more accurate on high-dimension
        data like word counts.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load data
df = pd.read_csv("emails.csv")
df = df.drop(columns=["Email No."])          # just an ID
df = df.dropna()

X = df.drop(columns=["Prediction"])          # word counts
y = df["Prediction"]                         # 1 = Spam, 0 = Not Spam

# 2. Split and scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 3. Train both models
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
svm = SVC(kernel="linear").fit(X_train, y_train)

# 4. Evaluate and compare
for name, model in [("KNN", knn), ("SVM", svm)]:
    pred = model.predict(X_test)
    print("=====", name, "=====")
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred))
