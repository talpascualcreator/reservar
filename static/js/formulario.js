function submitForm(event, endpoint) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const jsonData = Object.fromEntries(formData.entries());

    fetch(`http://127.0.0.1:5000/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(jsonData),
    })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error('Error:', error));
}

