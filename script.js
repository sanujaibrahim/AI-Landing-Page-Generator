async function generatePage() {
    const idea = document.getElementById("idea").value;
    const result = document.getElementById("result");

    if (!idea.trim()) {
        result.innerText = "Enter a business idea";
        return;
    }

    result.innerText = "Generating...";

    try {
        const response = await fetch("http://127.0.0.1:5000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ idea: idea })
        });

        const data = await response.json();

        result.innerHTML = `
            <h2>${data.title}</h2>
            <p>${data.description}</p>

            <h3>Features</h3>
            <p>${data.features.join(" • ")}</p>

            <button>Get Started</button>
        `;

    } catch (error) {
        result.innerText = "Connection error";
        console.error(error);
    }
}