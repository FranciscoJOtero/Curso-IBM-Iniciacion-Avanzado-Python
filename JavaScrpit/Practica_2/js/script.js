//CONVERSOR DE TEMPERATURAS
//Solicitamos datos a través del prompt
// let temp = parseFloat(prompt("Introduce la temperatura: "));
// let escala = prompt("Introduce escala a la que quiere convertir tu temperatura: ");
// //Condicional para realizar una cosa u otra en función de los datos introducidos
// if(escala === "Celsius" || escala ==="celsius") {
//     //Preguntamos desde que escala se va a convertir
//     let escalaOriginal = prompt("Introduce la escala original, Farenheit o Kelvin: ");
//     if(escalaOriginal === "Farenheit" || escalaOriginal === "farenheit") {
//         //fórmula para convertir de Farenheit a Celsius
//         let temp_celsius = (temp - 32) * 5/9;
//         //Mostrar en consola el resultado
//         console.log("Tu temperatura en Celsius es de: " + temp_celsius + " grados");
//     }else if(escalaOriginal === "Kelvin" || escalaOriginal === "kelvin") {
//         //fórmula para convertir de Kelvin a Celsius
//         temp_celsius = temp - 273.15;
//         //Mostrar en consola el resultado
//         console.log("Tu temperatura en Celsius es de: " + temp_celsius + " grados");
        
//     }else{
//         alert("Escala original no válida");
//     }
// }else if(escala === "Farenheit" || escala === "farenheit") {
//     //Preguntamos desde que escala se va a convertir
//     escalaOriginal = prompt("Introduce la escala original, Celsius o Kelvin: ");
//     if (escalaOriginal === "Celsius" || escalaOriginal === "celsius") {
//         //fórmula para convertir de  Celsius a Farenheit
//         let temp_farenheit = (temp * 9/5) + 32;
//         //Mostrar en consola el resultado
//         console.log("Tu temperatura en Farenheit es: " + temp_farenheit);
//     }else if(escalaOriginal === "Kelvin" || escalaOriginal === "kelvin"){
//         //fórmula para convertir de Kelvin a Farenheit
//         temp_farenheit = ((temp - 273.15) * 9/5) + 32;
//         //Mostrar en consola el resultado
//         console.log("Tu temperatura en Farenheit es: " + temp_farenheit);
//     }else {
//         alert("Escala original no válida");
//     }
    
// } else if(escala === "Kelvin" || escala ==="kelvin"){
//     //Preguntamos desde que escala se va a convertir
//     let escalaOriginal = prompt("Introduce la escala original de tus datos, Celsius o Farenheit: ");
//     //Condicional para realizar una cosa u otra en función de los datos introducidos
//     if(escalaOriginal === "Celsius" || escalaOriginal === "celsius"){
//         //fórmula para convertir de  Celsius a Kelvin
//         temp_kelvin = temp + 273.15;
//         //Mostrar en consola el resultado
//         console.log("Tu temperatura en Kelvin es de: " + temp_kelvin + ("K"));
//     } else if(escalaOriginal == "Farenheit" || escalaOriginal === "farenheit") {
//         //fórmula para convertir de  Farenheit a Kelvin
//         temp_kelvin = ((temp - 32) * 5/9) + 273.15;
//         //Mostrar en consola el resultado
//         console.log("Tu temperatura en Kelvin es de: " + temp_kelvin + ("K"));
//     } else {
//         //En caso de que los datos que introduzcan sean erróneos
//         alert("Escala original no válida");
//     }
// }else {
//     //En caso de que los datos que introduzcan sean erróneos
//     alert("Los datos introducidos son incorrectos");
// }


//ESTA PARTE ES MEJORADA, PARA INTERACTUAR CON LA INTERFAZ REALIZADA EN HTML

document.getElementById("convertir").addEventListener("click", () =>{
    const temperatura = parseFloat(document.getElementById("temperatura").value)
    const escalaOriginal = document.getElementById("escalaOriginal").value
    const escalaDestino = document.getElementById("escalaDestino").value
    let resultado;

    if(isNaN(temperatura)){
        document.getElementById("resultado").textContent = "Por favor, ingresa una temperatura válida."
        return;
    }
    
    if(escalaOriginal === escalaDestino) {
        document.getElementById("resultado").textContent = "Las escalas deben ser diferentes."
        return;
    }

    if(escalaOriginal === "celsius" && escalaDestino === "farenheit"){
        resultado = (temperatura * 9 / 5) + 32;
    }else if (escalaOriginal === "celsius" && escalaDestino ==="kelvin"){
        resultado = temperatura + 273.15;
    }else if(escalaOriginal === "farenheit" && escalaDestino === "celsius"){
        resultado = (temperatura - 32) * 5 / 9;
    }else if(escalaOriginal === "farenheit" && escalaDestino === "kelvin"){
        resultado = ((temperatura - 32) * 5 / 9) + 273.15;
    }else if(escalaOriginal === "kelvin" && escalaDestino === "celsius"){
        resultado = temperatura - 273.15;
    }else if(escalaOriginal === "kelvin" && escalaDestino === "farenheit"){
        resultado = ((temperatura - 273.15) * 9 / 5) + 32;
    }

    document.getElementById("resultado").textContent = `Resultado: ${resultado.toFixed(2)} ${escalaDestino.toUpperCase()}`;
});