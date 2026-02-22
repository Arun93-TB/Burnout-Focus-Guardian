function analyze() {
    const data = {
        sleep: document.getElementById("sleep").value,
        work: document.getElementById("work").value,
        mood: document.getElementById("mood").value,
        meetings: document.getElementById("meetings").value,
        caffeine: document.getElementById("caffeine").value
    };

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("result").innerHTML = `
            <h3>Risk Score: ${result.risk_score}</h3>
            <h3>Risk Level: ${result.risk_level}</h3>
            <p><b>Causes:</b> ${result.causes.join(", ")}</p>
            <p><b>My Advice:</b><br> ${result.actions.join("<br>")}</p>
        `;
    });
}
