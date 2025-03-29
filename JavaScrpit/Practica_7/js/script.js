// EJERCICIO DE ADIVINAR EL NÚMERO ALEATORIO QUE GENERA EL PRGRAMA

//inicializar el número aleatorio entre 1 y 100
const numeroAleatorio = Math.floor(Math.random() * 100) + 1;
console.log(numeroAleatorio);

//incializar número de intentos del usuario
let intentos = 0;

//Obtener elementos del DOM
const adivinanzaInput = document.getElementById("adivinanza");
const adivinarBoton = document.getElementById("adivinar");
const mensaje = document.getElementById("mensaje");
const intentosElemento = document.getElementById("intentos")

//Función para obtener el número que introduzca el usuario
function numeroUsuario(){
    return parseInt(prompt("Adivina el número que se genera entre 1 y 100: "));
}

//Función para verificar el número aleatorio
function verificarNumero(numUser){
    if(isNaN(numUser) || numUser < 1 || numUser > 100){
        mensaje.textContent = "Por favor, introduzca un número entre 1 y 100";
        return false;
    }

    //Incrementar el número de intentos
    intentos++;
    intentosElemento.textContent = `Intentos ${intentos}`

    if (numUser === numeroAleatorio) {
        mensaje.textContent= `OLÉ!!! Has acertado el número en ${intentos} intentos!Eres un crack`;
        adivinarBoton.disabled = true;
        return true;
    } else if(numUser < numeroAleatorio) {
        mensaje.textContent = `El número es mayor, prueba otra vez.`;
        
    } else if (numUser > numeroAleatorio) {
        mensaje.textContent = `El número es menor, prueba otra vez.`;
    }

    return false;
}

//Agregar evento al botón "Adivinar"
adivinarBoton.addEventListener("click", () =>{
    const adivinanzaUsuario = parseInt(adivinanzaInput.value);
    verificarNumero(adivinanzaUsuario);
});
