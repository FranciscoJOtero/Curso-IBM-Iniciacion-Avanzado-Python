//*EJERCICIO DE GENERAR CONTRASEÑAS ALEATORIAS

// function generarContraseña(longitud, mayusculas, minusculas, numeros, simbolos) {
//     let caracteres = "";
//     if (mayusculas) caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//     if (minusculas) caracteres += "abcdefghijklmnopqrstuvwxyz";
//     if (numeros) caracteres += "0123456789";
//     if (simbolos) caracteres += "!@#&*_-.?";

//     if (caracteres === "") {
//         return "Selecciona al menos un tipo de caracter.";
//     }

//     let contraseña = "";
//     for (let i = 0; i < longitud; i++) {
//         let caracterAleatorio = caracteres[Math.floor(Math.random() * caracteres.length)];
//         contraseña += caracterAleatorio;
//     }
//     return contraseña;
// }

// document.getElementById("generar").addEventListener("click", () => {
//     let longitud = parseInt(document.getElementById("longitud").value);
//     let mayusculas = document.getElementById("mayusculas").checked;
//     let minusculas = document.getElementById("minusculas").checked;
//     let numeros = document.getElementById("numeros").checked;
//     let simbolos = document.getElementById("simbolos").checked;

//     // Validación de entrada
//     if (longitud === "") {
//         document.getElementById("contrasena").textContent = "Por favor, ingresa una longitud válida.";
//         return; // Detener la ejecución si la longitud está vacía
//     }

//     longitud = parseInt(longitud); // Convertir a número entero

//     if (isNaN(longitud) || longitud <= 0) {
//         document.getElementById("contrasena").textContent = "Por favor, ingresa una longitud válida (número mayor que 0).";
//         return; // Detener la ejecución si la longitud no es un número válido
//     }

//     let contrasena = generarContraseña(longitud, mayusculas, minusculas, numeros, simbolos);
//     document.getElementById("contrasena").textContent = contrasena;
// });

/*****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/

//*EN ESTA PARTE HEMOS INTENTADO MEJORAR EL CÓDIGO

//Esta funcion nos sirve para generar una letra minuscula aleatoria
//Utilizamos el codigo Ascii para generar dicha letra, ya que el codigo para las minusculas en el codigo ASCII va del 97 al 122
function minusculaAleatoria(){
    //Math.floor() sirve redondear el nº decimal hacia abajo al entero más cercano
    //Math.random() sirve para generar un nº decimal aleatorio entre 0 y 1(max - min + 1)
    let codigoAscii = Math.floor(Math.random() * (122 - 97 + 1) +97);
    //String.fromCharcode() sirve para convertir dicho numero aleatorio que generamos a un caracter
    return String.fromCharCode(codigoAscii);
}
//Funcion igual a la anterior, pero ahora para generar mayusculas(en codigo ASCII van del 65 al 90)
function mayusculaAleatoria(){
    let codigoAscii = Math.floor(Math.random() * (90 - 65 + 1) + 65);
    return String.fromCharCode(codigoAscii);
}
//Esta para generar numero aleatorio entre 0 y 9(codigo ASCII van del 48 al 57)
function numeroAleatorio(){
    let codigoAscii = Math.floor(Math.random() * (57 - 48 + 1) + 48);
    return String.fromCharCode(codigoAscii);
}

//Para generar simbolos aleatorios, crearemos una cadena con los simbolos que queremos incluir
function simboloAleatorio(){
    const simbolos = "!@#*+=:.?-_";
    return simbolos[Math.floor(Math.random() * simbolos.length)];
}

// Una función para indicar el nivel de seguridad de la contraseña generada(debil, media y fuerte)

function calcularSeguridad(contrasenia){
    const longitud = contrasenia.length; // Una variable para guardar el valor de la longitud de la contraseña
    const mayusculas = /[A-Z]/.test(contrasenia);// Verificiar si hay mayusuclas en la contraseña
    const minusculas = /[a-z]/.test(contrasenia); // Verificiar si hay minusculas en la contraseña
    const numeros = /[0-9]/.test(contrasenia); // Verificiar si hay números en la contraseña
    const tieneSimbolos = /[!@#*_\-+=:.?]/.test(contrasenia); // Verificiar si hay simbolos en la contraseña

    let puntuacion = 0; // Variable para sumar la puntuacion obtenida en la contraseña

    //Una serie de condicionales para sumar un punto en caso de que en la contraseña se cumplan esos requisitos
    if(longitud >= 12) puntuacion++;

    if(mayusculas) puntuacion++;
    if(minusculas) puntuacion++;
    if(numeros) puntuacion++;
    if(tieneSimbolos) puntuacion++;
    //console.log(puntuacion); Para depurar errores a través de la consola
    //console.log(tieneSimbolos); Para depurar errores a través de la consola
    
    // Otra serie de condicionales para comprobar el nivel de seguridad de la contraseña
    if(puntuacion >= 5)return "Fuerte";
    
    if(puntuacion >= 4)return "Media";
    return "Débil";
}
//Ahora que tenemos funciones para generar diferentes tipos de caracteres aleatorios, vamos a combinarlas para crear un generador de contraseñas
function generarContrasena(longitud, mayusculas, minusculas, numeros, simbolos) {
    let funciones = [];// declaramos un array 

    if (mayusculas) {
        funciones.push(mayusculaAleatoria); //Agrega al array funciones, la función que genera mayusculas
    }
    if (minusculas) {
        funciones.push(minusculaAleatoria); //Agrega al array funciones, la función que genera minusculas
    if (numeros) {
        funciones.push(numeroAleatorio);//Agrega al array funciones, la función que genera numeros
    }
    if (simbolos) {
        funciones.push(simboloAleatorio);//Agrega al array funciones, la función que genera simbolos
    }

    if (funciones.length === 0) {//Para evitar que se genere una contraseña vacia.
        return "Selecciona al menos un tipo de caracter.";
    }

    let contraseña = "";// Variable que contendrá la contraseña que se genere
    //El bucle for se ejecutará tantas veces como caracteres vaya a tener la contraseña(variable longitud).
    for (let i = 0; i < longitud; i++) {
        //En cada iteracion del bucle, se selecciona una funcion aleatoria del array funciones
        let funcionAleatoria = funciones[Math.floor(Math.random() * funciones.length)];
        //La funcion seleccionada se ejecuta y su resultado se concatena en la variable contraseña
        contraseña += funcionAleatoria(); // Llamar a la función aleatoria
    }
    return contraseña;
    }
}

//Evento de click, al hacer click en el boton generar(html) se genera la contraseña
document.getElementById("generar").addEventListener("click", () =>{
    //declaramos las variables de cada input y checkbox del html para tenerlos localizados a cada uno
    let longitud = document.getElementById("longitud").value;//longitud de la contraseña
    let mayusculas = document.getElementById("mayusculas").checked;//incluir mayusculas
    let minusculas = document.getElementById("minusculas").checked;//incluir minusculas
    let numeros = document.getElementById("numeros").checked;//incluir numeros
    let simbolos = document.getElementById("simbolos").checked;//incluir simbolos

    //Condicional para asegurarnos que se indica el tamaño de la contraseña
    if(longitud === ""){
        document.getElementById("contrasena").textContent = "Ingresa un valor para la longitud de tu contraseña";
        return
    }
    //Convertimos longitud que es un string a un número
    longitud = parseInt(longitud);
    //Si longitud no es un numero o igual o inferior a cero, mensaje de error(validar campo longitud)
    if(isNaN(longitud) || longitud <=0){
        document.getElementById("contrasena").textContent = "Ingresa un valor para la longitud de tu contraseña";
        return
    }

    //Generamos la contraseña con la funcion generarContrasena y con los parámetros obtenidos
    let contrasena = generarContrasena(longitud,mayusculas, minusculas, numeros, simbolos);
    //Mostramos en la web la contraseña generada
    document.getElementById("contrasena").textContent = contrasena;
    //Mostramos en la web un mensaje con el nivel de seguridad de la contraseña
    document.getElementById("seguridad").textContent = "Seguridad: " + calcularSeguridad(contrasena);
});
//Selecciona el elemento del DOM con el ID "copiar" (botón)
// y le agrega un evento de click. Cuando el usuario haga clic en este elemento,
// se ejecutará la función de flecha (arrow function) que sigue.
document.getElementById("copiar").addEventListener("click", () =>{
    //Obtenemos el contenido de texto del elemento con el ID "contrasena".
    // Este elemento muestra la contraseña generada en la interfaz(web).
    const contrasenia = document.getElementById("contrasena").textContent;
    /// Verificamos si el contenido de "contrasenia" no está vacío.
    // Si hay una contraseña generada, se procede a copiarla al portapapeles.
    if(contrasenia){
        // Usamos la API del portapapeles para copiar el texto de "contrasenia".
        // navigator.clipboard.writeText() es una promesa que intenta copiar el texto.
        navigator.clipboard.writeText(contrasenia)
        .then(() => {
            // Si la copia es exitosa, se ejecuta este bloque.
            //La API navigator.clipboard solo funciona en contextos seguros (HTTPS o localhost).
            //Con esto enviamos un mensaje al usuario para que sepa que su navegador no soporta esta API
            if (!navigator.clipboard) {
                alert("Tu navegador no soporta la funcionalidad de copiar al portapapeles.");
                return;
            }else{
                // Muestra una alerta al usuario indicando que la contraseña se copió correctame
                alert("Contraseña copiada al portapapeles")
            }
        })
        .catch((error) =>{
            //Si ocurre un error al intentar copiar la contraseña, se ejecuta este bloque.
            // Muestra el error en la consola para fines de depuración.
            console.log("Error al copiar la contraseña", error);
            // Muestra una alerta al usuario indicando que no se pudo copiar la contraseña.
            alert("No se pudo copiar la contraseña");
            
        });
    }
})