function analyzeRisk() {

    var amount = document.getElementById("amount").value;
    var location = document.getElementById("location").value;
    var time = document.getElementById("time").value;
    var transactions = document.getElementById("transactions").value;

    if (amount == "" || location == "" || time == "" || transactions == "") {
        document.getElementById("result").innerHTML =
            "<p>Please enter all transaction details.</p>";
        return;
    }

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            amount: amount,
            location: location,
            time: time,
            transactions: transactions
        })
    })

    .then(response => response.json())

    .then(data => {

        var riskLevel;

        if (data.risk_percentage >= 70) {
            riskLevel = "HIGH";
        }
        else if (data.risk_percentage >= 40){
            riskLevel = "MEDIUM";
        }
        else {
            riskLevel = "LOW";
        }
        document.getElementById("result").innerHTML =
            "<h2>AI Risk Level: " + riskLevel + "</h2>" +
            "<p><b>AI Decision:</b> " + data.result + "</p>" +
            "<p><b>Detection Method:</b> Random Forest ML Model 🤖</p>" +
            "<p><b>Recommendation:</b> Review this transaction before approving it.</p>";
            var reasonText = data.reasons.join("<br>");

document.getElementById("result").innerHTML +=
    "<p><b>AI Risk Factors:</b><br>" + reasonText + "</p>";
           document.getElementById("riskBar").style.width =
    data.risk_percentage + "%";
  if (data.risk_percentage >= 70) {
    document.getElementById("riskBar").style.backgroundColor = "red";
}
else if (data.risk_percentage >= 40) {
    document.getElementById("riskBar").style.backgroundColor = "orange";
}
else {
    document.getElementById("riskBar").style.backgroundColor = "green";
}

document.getElementById("riskPercentage").innerHTML =
    data.risk_percentage + "%";

    })

    .catch(error => {

        document.getElementById("result").innerHTML =
            "<p>Unable to connect to the AI model. Please make sure the Flask server is running.</p>";

        console.log(error);
    });
}
