document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('api-spec');
    const formData = new FormData();
    formData.append('api-spec', fileInput.files[0]);

    const response = await fetch('http://localhost:5000/run-tests', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('output').textContent = JSON.stringify(result, null, 2);
});
