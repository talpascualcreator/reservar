function submitForm(event) {
    event.preventDefault();  // Evitamos que el formulario se envíe inmediatamente.

    // Llamamos a SweetAlert o cualquier otra acción antes de enviar el formulario
    Swal.fire({
        title: "Operación realizada exitosamente",
        icon: "success",
        draggable: true
    }).then((result) => {
        // Después de que el usuario vea el mensaje, enviamos el formulario de forma tradicional.
        if (result.isConfirmed) {
            event.target.submit();  // Ahora enviamos el formulario de manera tradicional.
        }
    });
}

