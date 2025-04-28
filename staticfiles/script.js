async function fetchEntrepreneurs(industry) {
    try {
        const response = await fetch(`/strategy/api/entrepreneurs/?industry=${encodeURIComponent(industry)}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching entrepreneurs:', error);
        return [];
    }
}

async function displayEntrepreneurs(industry) {
    const experts = await fetchEntrepreneurs(industry);
    const expertsContainer = document.getElementById('experts-container');
    expertsContainer.innerHTML = '';

    if (experts.length === 0) {
        expertsContainer.innerHTML = '<p>No entrepreneurs found for this industry.</p>';
        return;
    }

    experts.forEach(expert => {
        const expertDiv = document.createElement('div');
        expertDiv.classList.add('expert-suggestion');

        expertDiv.innerHTML = `
            <img src="${expert.image}" alt="${expert.name}" class="expert-img">
            <div class="expert-info">
                <h4>${expert.name} - ${expert.company}</h4>
                <p>Expertise: ${expert.expertise}</p>
            </div>
        `;

        expertsContainer.appendChild(expertDiv);
    });
}

async function displayResults(strategy) {
    loadingSection.style.display = 'none';
    resultsSection.classList.add('active');

    // Display strategy
    strategyOutput.innerHTML = strategy;

    // Display successful entrepreneurs
    await displayEntrepreneurs(answers.industry);
}