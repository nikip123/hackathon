
document.getElementById('api-spec').addEventListener('change', (event) => {
    const fileNameElement = document.getElementById('file-name');
    const file = event.target.files[0];
    if (file) {
        fileNameElement.textContent = `Selected file: ${file.name}`;
    } else {
        fileNameElement.textContent = 'No file chosen';
    }
});


document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('api-spec');
    const formData = new FormData();
    const outputElement = document.getElementById('output');
    const resultsElement = document.getElementById('results');

    if (fileInput.files.length === 0) {
        resultsElement.insertAdjacentHTML('beforeend', '<p class="error">Please select a file before submitting.</p>');
        return;
    }

    formData.append('api-spec', fileInput.files[0]);

    try {
        const response = await fetch('http://localhost:8080/run-tests/', {
            method: 'POST',
            body: formData,
        });

        resultsElement.querySelectorAll('p').forEach(p => p.remove()); 

        if (response.ok) {
            const result = await response.json();
            outputElement.textContent = result.message || "Tests completed!";
            resultsElement.insertAdjacentHTML('beforeend', '<p class="success">File was successfully submitted.</p>');
        } else {
            console.error("Failed to fetch data from backend:", response.statusText);
            resultsElement.insertAdjacentHTML('beforeend', '<p class="error">File submission failed. Please try again.</p>');
        }
    } catch (error) {
        console.error("Error during fetch:", error);
        resultsElement.insertAdjacentHTML('beforeend', '<p class="error">An error occurred while submitting the file.</p>');
    }
});
