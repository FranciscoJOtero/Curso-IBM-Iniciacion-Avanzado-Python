const tarea = document.getElementById("tarea");
const crear = document.getElementById("crear");
const lista = document.getElementById("lista_tareas");

document.getElementById("crear").addEventListener("click", () =>{
    const textoTarea = tarea.value;
    
    if(textoTarea.trim() === ""){
        document.getElementById("error").textContent = "Introduzca su nueva tarea por favor";
        return;
    }

    const nuevaTarea = document.createElement("LI");
    nuevaTarea.textContent = textoTarea;

    lista.appendChild(nuevaTarea);
    tarea.value = "";
    
});