//PRÁCTICAS INICIALES SENCILLAS
//Solicitar al usuario por promt su año de nacimiento, calcular su edad y mostrarlo mediante console.log

// let anyo= parseInt(prompt("Introduce tu año de nacimiento"));
// let anyo_actual = new Date().getFullYear();
// let edad = anyo_actual - anyo;
// console.log("Tu edad actual es de " + edad + (" años"));

//Declaro 3 variables, una para el año de nacimiento que introduce el usuario, otra para obtener el año actual, y una tercera
//para calcular su edad actual, se podría simplificar más y ahorrarnos alguna variable...

//Mismo ejercicio, pero ahora solicitando datos y mostrandolos en la web utilizando el DOM

document.getElementById("calcular").addEventListener("click", function() {
    let anioNacimiento = parseInt(document.getElementById("anio_nac").value);
    let anioActual = new Date().getFullYear();
    let edadUsuario = anioActual - anioNacimiento;

    if(isNaN(edadUsuario)) {
        document.getElementById("resultado").textContent = "Introduzca un año válido por favor";
    } else if(anioNacimiento > anioActual){
        document.getElementById("resultado").textContent = "Edad no válida";
    }else if (anioNacimiento <= 0){ 
        document.getElementById("resultado").textContent = "Edad no válida";
    }else {
        document.getElementById("resultado").textContent = "Tu edad es de " + edadUsuario + " años";
    }
});

