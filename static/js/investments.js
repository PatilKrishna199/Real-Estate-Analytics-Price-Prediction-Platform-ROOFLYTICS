async function fetchInvestmentOpportunities() {
    try {
        let response = await fetch('/api/investments');
        let data = await response.json();
        let investmentCards = document.getElementById('investmentCards');
        investmentCards.innerHTML = '';

        data.forEach(property => {
            let card = `
                <div class="card">
                    <h3>${property.name} - ${property.location}</h3>
                    <p><strong>Price:</strong> ₹${property.price.toLocaleString()}</p>
                    <p><strong>ROI:</strong> ${property.roi}% per annum</p>
                    <p><strong>Type:</strong> ${property.type}</p>
                    <button onclick="showInvestmentForm('${property.name}')">Invest Now</button>
                </div>
            `;
            investmentCards.innerHTML += card;
        });
    } catch (error) {
        console.error("Error fetching investments:", error);
    }
}

function showInvestmentForm(propertyName) {
    document.getElementById('investmentMessage').style.display = "none";
    document.getElementById('investorName').value = "";
    document.getElementById('investorEmail').value = "";
    document.getElementById('investmentAmount').value = "";
    document.getElementById('investmentForm').style.display = "block";
}

async function submitInvestment() {
    let investorName = document.getElementById('investorName').value;
    let investorEmail = document.getElementById('investorEmail').value;
    let investmentAmount = document.getElementById('investmentAmount').value;

    if (!investorName || !investorEmail || !investmentAmount) {
        alert("Please fill in all fields.");
        return;
    }

    try {
        let response = await fetch('/api/invest', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: investorName,
                email: investorEmail,
                amount: investmentAmount
            })
        });

        if (response.ok) {
            document.getElementById('investmentMessage').style.display = "block";
        }
    } catch (error) {
        console.error("Error submitting investment:", error);
    }
}

fetchInvestmentOpportunities();
