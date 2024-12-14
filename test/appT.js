document.getElementById('get-pets').addEventListener('click', async () => {
    const response = await fetch('http://localhost:5000/pets');
    const data = await response.json();
    const petsListDiv = document.getElementById('pets-list');
    petsListDiv.innerHTML = '<h3>Pets List:</h3>';
    data.forEach(pet => {
        petsListDiv.innerHTML += `<p>${pet.id}. ${pet.name} (${pet.species})</p>`;
    });
});

document.getElementById('create-pet').addEventListener('click', async () => {
    const name = document.getElementById('pet-name').value;
    const species = document.getElementById('pet-species').value;

    const response = await fetch('http://localhost:5000/pets', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, species })
    });

    if (response.ok) {
        const pet = await response.json();
        alert(`Pet created: ${pet.name}`);
    } else {
        alert('Failed to create pet');
    }
});

document.getElementById('delete-pet').addEventListener('click', async () => {
    const petId = document.getElementById('pet-id').value;

    const response = await fetch(`http://localhost:5000/pets/${petId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        alert(`Pet with ID ${petId} deleted successfully`);
    } else {
        alert('Failed to delete pet');
    }
});
