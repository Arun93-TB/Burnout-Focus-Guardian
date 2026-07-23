function analyze() {

    const data = {
        sleep: document.getElementById("sleep").value,
        work: document.getElementById("work").value,
        mood: document.getElementById("mood").value,
        meetings: document.getElementById("meetings").value,
        caffeine: document.getElementById("caffeine").value
    };

    fetch("https://burnout-focus-guardian-4.onrender.com/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Server Error");
        }
        return response.json();
    })
    .then(result => {

        document.getElementById("result").innerHTML = `
            <h3>Risk Score: ${result.risk_score}</h3>
            <h3>Risk Level: ${result.risk_level}</h3>
            <h3>Health Score: ${result.health_score}</h3>

            <p><b>Causes:</b><br>${result.causes.join("<br>")}</p>

            <p><b>Advice:</b><br>${result.actions.join("<br>")}</p>

            <p><b>Motivation:</b><br>${result.motivation}</p>

            <p><b>Wellness Tip:</b><br>${result.wellness_tip}</p>

            <p><b>Time:</b> ${result.analysis_time}</p>
        `;

    })
    .catch(error => {
        console.error(error);

        document.getElementById("result").innerHTML =
        "<h2 style='color:red;'>Unable to connect to Flask Backend</h2>";
    });

}