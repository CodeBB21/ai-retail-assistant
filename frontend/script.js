document.getElementById("predictForm").addEventListener("submit", async function(e){
    e.preventDefault();

    const data = {
        age: parseFloat(document.getElementById("age").value),
        income: parseFloat(document.getElementById("income").value),
        amount: parseFloat(document.getElementById("amount").value),
        frequency: parseFloat(document.getElementById("frequency").value),
        last_purchase_days_ago: parseFloat(document.getElementById("last").value),
        gender: document.getElementById("gender").value,
        city: document.getElementById("city").value,
        category: document.getElementById("category").value
    };

    const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText =
        "Prédiction : " + result.prediction;
});
