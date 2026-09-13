import csv
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix,f1_score

data = []

with open("data/transactions.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

locations = {
    "Hyderabad": 0,
    "Mumbai": 1,
    "Delhi": 2,
    "Chennai": 3,
    "Bangalore": 4
}

X = []
y = []

for row in data:

    hour = int(row["time"].split(":")[0])

    X.append([
        float(row["amount"]),
        locations[row["location"]],
        hour,
        int(row["transactions"])
    ])

    y.append(int(row["is_fraud"]))


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1=f1_score(y_test, predictions)

cm = confusion_matrix(y_test, predictions)

print("Precision:", precision * 100, "%")
print("Recall:", recall * 100, "%")
print("Confusion Matrix:")
print("F1 Score:", f1 * 100, "%")
print(cm)

false_positive_cost = 0

for i in range(len(y_test)):
    if y_test[i] == 0 and predictions[i] == 1:
        false_positive_cost += X_test[i][0]

print("False Positive Cost: ₹", false_positive_cost)

print("Model trained successfully!")
print("Training transactions:", len(X_train))
print("Testing transactions:", len(X_test))
print("Accuracy:", accuracy * 100, "%")

with open("fraud_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("New fraud_model.pkl saved successfully!")
