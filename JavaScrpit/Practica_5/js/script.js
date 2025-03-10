// Ejercicio muy sencillo que cuenta las vocales de una cadena y lo muestra por consola
// function contarVocales(cadena){
//     const cadenaMinusculas = cadena.toLowerCase();
//     let contador = 0;

//     for(let i=0;i < cadena.length; i++){
//         if(cadena[i] === "a" || cadena[i] ==="e" || cadena[i] === "i" || cadena[i] === "o" || cadena[i] === "u") {
//             contador++;
//         }
//     }
//     return contador;
// }

// const texto = "Hola mundo";
// const numeroVocales = contarVocales(texto);
// console.log("El texto contiene " + numeroVocales + " vocales.");
//**********************************************************************************************************************************************//
//************************************************************************************************************************************************//
//MISMO EJERCICIO
//creamos interfaz gráfica para interactuar con ella

function contarVocales(cadena){
    const cadenaMinusculas = cadena.toLowerCase();
    let contador = 0;

    for(const caracter of cadenaMinusculas){
        if(caracter === "a" || caracter ==="e" || caracter === "i" || caracter === "o" || caracter === "u"){
            contador++;
        }
    }
    return contador;
}

document.getElementById("contar").addEventListener("click", () =>{
    const cadena = document.getElementById("texto").value;
    //console.log(cadena);
    const contar = contarVocales(cadena);
    //console.log(contar);
    if(cadena === ""){
        document.getElementById("resultado").textContent = "Escribe algo antes de dar al botón!!";
    } else {
        document.getElementById("resultado").textContent = `Número de vocales: ${contar}`;
        document.getElementById("resultado").style.animation = "fadeIn 0.5s";
    }
});

document.getElementById("texto").addEventListener("input", () =>{
    const max = 500;
    const current = document.getElementById("texto").value.length;
    //console.log(current);
    if(current === max){
        document.getElementById("contador").textContent = `Has llegado al máximo de caracteres permitidos(${current} caracteres).`;
    }else {
        document.getElementById("contador").textContent = `${current}/${max} caracteres`;
    }
    if(current > max - 10){
        document.getElementById("contador").style.color = "#e74c3c"
    }else {
        document.getElementById("contador").style.color = "#7f8c8d"
    }
});

document.getElementById("tema-oscuro").addEventListener("change", (e) => {
    document.body.classList.toggle("dark", e.target.checked);
    localStorage.setItem("tema-oscuro", e.target.checked); // Guarda la preferencia
});

// Carga el tema guardado
const temaGuardado = localStorage.getItem("tema-oscuro") === "true";
document.getElementById("tema-oscuro").checked = temaGuardado;
document.body.classList.toggle("dark", temaGuardado);