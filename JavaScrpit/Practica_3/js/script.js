//Ejercicio sencillo para comprobar si un nº es par o impar
document.getElementById("verificar").addEventListener("click", function(){
    let numero = parseInt(document.getElementById("numero").value);
    let resultado = verificarNumero(numero);
    document.getElementById("resultado").textContent = resultado;
});

function verificarNumero(numero) {
    if(numero % 2 === 0) {
        return "El número introducido es par!";
    }else {
        return "El número introducido es impar!";
    }
}