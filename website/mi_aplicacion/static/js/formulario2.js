const form = document.getElementById('formulario')

form.addEventListener('submit', function(event){
    event.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const telefono = document.getElementById('telefono').value;
    const correo = document.getElementById('correo').value;
    const contraseña = document.getElementById('contraseña').value;

    if(nombre === ''){
        alert('El campo "nombre" está vacío');
        return;
    }

    if(telefono === ''){
        alert('El campo "teléfono" está vacío');
        return;
    }

    if(correo === ''){
        alert('El campo "correo" está vacío');
        return;
    }

    if(contraseña === ''){
        alert('El campo "contraseña" está vacío');
        return;
    }

    alert('Registro Exitoso');
    form.reset();
});