import csv
import random

random.seed(42)

locations = ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Bangalore"]

with open("data/transactions.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "amount",
        "location",
        "time",
        "transactions",
        "is_fraud"
    ])

    for i in range(1000):

        amount = random.randint(500, 70000)
        location = random.choice(locations)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        time = f"{hour:02d}:{minute:02d}"
        transactions = random.randint(1, 12)

        risk = 0

        if amount >= 40000:
            risk += 1

        if hour < 5:
            risk += 1

        if transactions >= 7:
            risk += 1

        if risk >= 2:
            is_fraud = 1
        else:
            is_fraud = 0

        # Add 10% random noise
        if random.random() < 0.10:
            is_fraud = 1 - is_fraud

        writer.writerow([
            amount,
            location,
            time,
            transactions,
            is_fraud
        ])

print("New realistic dataset created successfully!")
print("Total transactions: 1000")
