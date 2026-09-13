import pickle

with open("fraud_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Fraud detection model loaded successfully!")
amount = 60000
location = 2
time = 2
transactions = 8

new_transaction = [[amount, location, time, transactions]]

prediction = model.predict(new_transaction)

if prediction[0] == 1:
    print("Result: Potential Fraud ⚠️")
else:
    print("Result: Normal Transaction ✅")
