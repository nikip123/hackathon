document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('api-spec');
    const formData = new FormData();
    formData.append('api-spec', fileInput.files[0]);

    try {
        const response = await fetch('http://localhost:5000/run-tests', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('output').textContent = JSON.stringify(result, null, 2);
        } else {
            console.error("Failed to fetch data from backend:", response.statusText);
        }
    } catch (error) {
        console.error("Error during fetch:", error);
    }
});
