document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('api-spec');
    const formData = new FormData();
    formData.append('api-spec', fileInput.files[0]);

    try {
        const response = await fetch('http://localhost:8080/run-tests/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            document.getElementById('output').textContent = await response.json();
        } else {
            console.error("Failed to fetch data from backend:", response.statusText);
        }
    } catch (error) {
        console.error("Error during fetch:", error);
    }
});
