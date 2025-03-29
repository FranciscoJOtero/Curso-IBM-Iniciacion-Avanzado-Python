//EJERCICIO DE VALIDAR FORMULARIOS JAVASCRIPT

//DOMContentLoaded se activa cuando el HTML ha sido completamente cargado y procesado por el navegador.
//Esto asegura que el script solo se ejecute cuando los elementos del formulario existan en la página.
document.addEventListener("DOMContentLoaded", function() {

    //Obtener elementos del DOM
    //Obtenemos el formulario por su ID
    const formulario = document.getElementById("registro_form");

    // Selecciona todos los inputs con la clase "container__input" y devuelve un Nodelist(similar a un array)
    const inputs = document.querySelectorAll(".container__input");

    // ✅ Verificar si los elementos existen antes de continuar
    //Se verifica que el formulario no sea null y que haya al menos un input en inputs.
    if (!formulario || inputs.length === 0) {

        //Si no hay formulario o inputs, se muestra un error en la consola 
        //console.error("⚠️ Error: No se encontraron elementos del formulario.");

        //el script se detiene con return.
        return;
    }

    //Expresión regular para validar email
    //Se define una expresión regular (regex) para validar emails.
    //  ^[^\s@]+ → El email no debe empezar con espacio o @.
    //  @[^\s@]+ → Debe contener una @ seguida de caracteres válidos.
    //  \.[^\s@]+$ → Debe tener un punto (.) seguido de más caracteres.
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    //Función para mostrar errores en cada campo, recibe un input y un mensaje de error.
    function mostrarError(input, mensaje) {

        //Busca el div correspondiente con el formato error-{id_del_input}.
        const errorDiv = document.getElementById(`error-${input.id}`);

        //Si existe, coloca el mensaje dentro del div.
        if (errorDiv) {
            errorDiv.textContent = mensaje;
        }
    }

    //Función para validar un solo campo
    function validarCampo(input) {

        //Obtenemos el valor del campo y eliminamos los espacios al inicio y al final.
        const valor = input.value.trim();

        //Variable para almacenar el mensaje de error.
        let error = "";

        //Condicional para comprobar i el nombre está vacío
        if (input.id === "nombre" && valor === "") {

            //Si esta vacio mensaje de error
            error = "El nombre es obligatorio.";
        
        //Comprobamos que el nombre no sea un número
        }else if (input.id === "nombre" && !isNaN(valor)){
            //Si es un número mensaje de error.
            error = "El nombre no puede ser un número.";
        
        //Verificamos que el formato del email es correcto con la expresión regular
        } else if (input.id === "email" && !emailRegex.test(valor)) {

            //en caso erróneo aviso al usuario
            error = "Ingrese un Email válido.";

        //Verificamos que la contraseña al menos tenga 6 caracteres.
        } else if (input.id === "password" && valor.length < 6) {

            //si no se cumple aviso al usuario con mensaje de error
            error = "La contraseña debe tener al menos 6 caracteres.";

        //Comprobar que las contraseñas coinciden
        } else if (input.id === "confirm_password" && valor !== document.getElementById("password").value) {

            //Si no coinciden, mensaje de error
            error = "Las contraseñas no coinciden.";
        }

        //Llamada a la funcion mostrarError() para mostrar los mensajes de error en el formulario.
        mostrarError(input, error);
    }

    //Agregar validación en tiempo real
    //por ejemplo: si el usuario escribe un email incorrecto, el mensaje de error aparecerá en tiempo real, sin necesidad de enviar el formulario.
    //Recorrer todos los inputs con el bucle forEach().
    inputs.forEach(input => {

        //Agrega un addEventListener("input", ...) a cada uno.
        //Cada vez que el usuario escriba algo, se ejecuta validarCampo()
        input.addEventListener("input", () => validarCampo(input));
    });

    //Validación del formulario
    formulario.addEventListener("submit", function(evento) {

        //Detiene el envío predeterminado del formulario para primero validar los datos.
        evento.preventDefault();

        //Variable que indicará si hay errores.
        let hayErrores = false;

        //Recorrer los inputs
        inputs.forEach(input => {

            //Y validar cada campo
            validarCampo(input);

            //Busca el div de error.
            const errorDiv = document.getElementById(`error-${input.id}`);
            if (errorDiv && errorDiv.textContent !== "") {
                hayErrores = true;
            }
        });

        //Si no hay errores, enviar el formulario
        if (!hayErrores) {

            //depuración en consola
            //console.log("Formulario enviado con éxito.");

            //Enviar formulario
            formulario.submit();
        }
    });
});
