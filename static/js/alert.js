function handleSubmit(event, endpoint) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const jsonData = Object.fromEntries(formData.entries());

    fetch(`http://127.0.0.1:5000${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(jsonData),
    })
        .then(response => response.json())
        .then(data => {
            // Mostrar alerta de éxito con SweetAlert2
            Swal.fire({
                title: '¡Éxito!',
                text: data.message,
                icon: 'success',
                confirmButtonText: 'OK',
                timer: 3000,
            });
            form.reset(); // Limpiar el formulario
        })
        .catch(error => {
            console.error('Error:', error);
            // Mostrar alerta de error con SweetAlert2
            Swal.fire({
                title: 'Error',
                text: 'Hubo un problema al enviar los datos. Intente nuevamente.',
                icon: 'error',
                confirmButtonText: 'OK',
            });
        });
}
