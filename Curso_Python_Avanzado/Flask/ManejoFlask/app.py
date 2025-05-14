#IMPORTACIONES
#Flask: Clase principal del framework Flask, usada para crear la aplicación web.
#redirect y url_for: Permiten redirigir a otras rutas y generar URLs dinámicas respectivamente.
#render_template: Se usa para renderizar archivos HTML con datos desde Python.
from flask import Flask, redirect, render_template, url_for
#ClienteForma: Clase que representa el formulario del cliente (usando Flask-WTF).
from cliente_forma import ClienteForma
#Cliente: Modelo de datos del cliente (una clase con atributos como id, nombre, etc.).
from cliente import Cliente
#ClienteDAO: Clase de acceso a datos para clientes 
#(DAO = Data Access Object), que permite hacer operaciones como insertar, actualizar, eliminar, seleccionar.
from cliente_dao import ClienteDAO

#INICIALIZACIÓN DE LA APP FLASK
#Se crea la aplicación Flask
app = Flask(__name__)
#Se configura una clave secreta necesaria para proteger formularios (CSRF en Flask-WTF).
app.config['SECRET_KEY'] = 'llave'
#Se define un título de la aplicación que se pasa a las plantillas HTML.
titulo_app = 'Zona Fit (GYM)'

#RUTAS
#Ruta raíz (/) y también /index.html apuntan a la misma función.
@app.route('/') #url: http://localhost:5000/
@app.route('/index.html')
#Esta línea define una función de vista en Flask llamada inicio.
#Se ejecutará automáticamente cuando el usuario acceda a la raíz de la aplicación web (/) 
#o a /index.html (según lo definido con los decoradores @app.route).
def inicio():

    #Se utiliza el sistema de logging de Flask para registrar un mensaje de depuración (nivel DEBUG).
    #Este mensaje aparece en la consola cuando se accede a esta ruta y el modo debug está activado.
    #Es útil para desarrolladores, ya que confirma que se está accediendo correctamente al path /.
    app.logger.debug('Entramos al path de inicio /')

    #recuperar clientes de la BBDD
    #Se recuperan los clientes de la base de datos con ClienteDAO.seleccionar().
    clientes_db = ClienteDAO.seleccionar()

    #crea una instancia de la clase ClienteForma, que representa un formulario web (probablemente construido con Flask-WTF).
    #Este formulario será usado para introducir los datos de un nuevo cliente o modificar uno existente.
    #En este punto, el formulario está vacío.
    cliente_forma = ClienteForma()

    #Se crea un nuevo objeto Cliente vacío, sin datos cargados.
    #Esta clase representa el modelo de cliente y contendrá atributos como id, nombre, email, etc.
    #Este objeto servirá de base para llenar el formulario con datos si fuera necesario.
    cliente = Cliente()

    #Se vuelve a crear el formulario cliente_forma, pero ahora asociado al objeto cliente vacío.
    #Esto se hace para que el formulario tenga la estructura esperada y esté preparado para auto-rellenarse 
    #en el futuro si el objeto cliente tuviera datos.
    #Esta línea sobrescribe el formulario anterior, pero esta vez con una estructura asociada a un modelo de datos.
    cliente_forma = ClienteForma(obj=cliente)

    #Se devuelve la plantilla index.html al navegador del usuario.
    #Además, se pasan varias variables al contexto de la plantilla:
        #titulo: el título de la aplicación web (en este caso, 'Zona Fit (GYM)').
        #clientes: la lista completa de clientes que se mostrarán en una tabla.
        #forma: el formulario ClienteForma, que se mostrará para añadir o editar un cliente.
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

#Este decorador indica que la función guardar() se ejecutará cuando se acceda a la URL /guardar mediante el método HTTP POST.
#Esta función recibe los datos enviados desde un formulario HTML que probablemente se encuentra en index.html.
#Al ser método POST, no se accede directamente desde la URL en el navegador, sino a través del envío de un formulario.
@app.route('/guardar', methods=['POST'])
#Se define la función guardar(), encargada de procesar los datos del formulario, 
#ya sea para crear un nuevo cliente o actualizar uno existente.
def guardar():
    #creamos los objetos de cliente, inicalmente vacios
    cliente = Cliente()

    #Crear una instancia del formulario ClienteForma, enlazada con el objeto cliente.
    #Esto permite que Flask-WTF asocie automáticamente los campos del formulario con los atributos del objeto cliente, 
    #facilitando la validación y la asignación de datos.
    cliente_forma = ClienteForma(obj=cliente)

    #Se comprueba si el formulario ha sido enviado correctamente y validado sin errores. Esto incluye que:
        #Se haya usado el método POST.
        #Se hayan cumplido todas las reglas de validación definidas en ClienteForma
    if cliente_forma.validate_on_submit():
        
        #Esta línea rellena el objeto cliente con los datos enviados desde el formulario.
        cliente_forma.populate_obj(cliente)

        #Se comprueba si el cliente no tiene un ID asignado (es decir, es un cliente nuevo).
        if not cliente.id:

            #Si el cliente es nuevo, se utiliza el método insertar() del ClienteDAO para guardar el nuevo cliente en la base de datos.
            ClienteDAO.insertar(cliente)

        #Si el cliente sí tiene un ID, significa que ya existe en la base de datos y lo que se desea es actualizar sus datos
        else:

            #Se llama al método actualizar() del ClienteDAO para modificar los datos del cliente existente en la base de datos.
            ClienteDAO.actualizar(cliente)

    #Después de guardar o actualizar el cliente, se redirecciona al usuario a la página de inicio (/).
    #url_for('inicio') genera automáticamente la URL del endpoint inicio, que es la función que muestra 
    #la plantilla index.html con la lista de clientes actualizada.
    return redirect(url_for('inicio'))

#Este decorador indica que la función limpiar() se ejecutará cuando el usuario acceda a la URL /limpiar.
#Esta ruta esta asociada a un botón “Limpiar” en el formulario de la web.
@app.route('/limpiar')

#Definir la función limpiar().
#Su propósito es restablecer el formulario y volver a la vista principal (inicio) con los campos vacíos.
#No realiza ninguna acción sobre la base de datos ni modifica datos del formulario directamente.
def limpiar():

    #Redirige al usuario de vuelta al inicio (/), donde se renderiza el formulario en blanco y se muestra la lista de clientes.
    #url_for('inicio') genera dinámicamente la URL correspondiente a la función inicio() para mayor seguridad y flexibilidad.
    #La redirección implica una nueva solicitud GET a la página de inicio, lo cual garantiza que el estado del formulario vuelva
    #a ser limpio, sin datos cargados anteriormente.
    return redirect(url_for('inicio'))

#Esta línea define una ruta dinámica que acepta un parámetro en la URL: el id del cliente a editar.
#si el usuario accede por ejemplo a /editar/5, el valor 5 se pasará como argumento a la función.
#El tipo int: indica que el valor debe ser un número entero, lo que ayuda a evitar errores y garantiza que el ID es válido.
@app.route('/editar/<int:id>')

#Definir la función editar() que recibe como argumento un id.
#El objetivo es cargar los datos del cliente con ese ID para prellenar el formulario, permitiendo al usuario modificarlos.
def editar(id):

    #Utilizamos el método seleccionar_por_id() del objeto ClienteDAO para obtener el cliente desde la base de datos 
    #cuyo id coincida con el recibido en la URL. El resultado es un objeto cliente ya cargado con los datos actuales que se desea editar.
    cliente = ClienteDAO.seleccionar_por_id(id)

    #Se crea un formulario ClienteForma que ya contiene los datos del cliente recuperado. Gracias a obj=cliente, 
    #el formulario se inicializa prellenado con los valores actuales del cliente, lo que permite al usuario 
    #ver los datos existentes y modificarlos fácilmente.
    cliente_forma = ClienteForma(obj=cliente)

    #Se obtiene nuevamente la lista completa de clientes desde la base de datos.Esto se hace porque
    #la plantilla index.html necesita tanto:
        #El formulario de edición con los datos del cliente seleccionado.
        #La lista de todos los clientes para mostrarla en la tabla, como en la vista principal.
    clientes_db = ClienteDAO.seleccionar()

    #Se renderiza la plantilla index.html, pasando las siguientes variables:
        #titulo=titulo_app: el título general de la aplicación (ej. "Zona Fit (GYM)").
        #clientes=clientes_db: la lista completa de clientes para mostrar en la tabla.
        #forma=cliente_forma: el formulario prellenado con los datos del cliente que se desea editar.
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

#Define una ruta dinámica que acepta un parámetro de tipo entero (id) desde la URL.
#Se activa cuando el usuario accede a una URL como /eliminar/3, donde 3 es el id del cliente que se desea borrar.
#Se llama desde un botón “Eliminar” en la interfaz.
@app.route('/eliminar/<int:id>')

#Define la función que se ejecutará al acceder a esa ruta. Recibe como argumento el id del cliente que se va a eliminar.
def eliminar(id):

    #Se crea un objeto Cliente con solo el atributo id asignado.
    #No se necesita cargar el resto de los datos del cliente (nombre, correo, etc.) para eliminarlo: basta con conocer su identificador.
    #Esto prepara el objeto para ser usado por el método eliminar().
    cliente = Cliente(id=id)

    #Llamada al método eliminar() del objeto ClienteDAO, pasando el cliente con su ID.
    #Este método se encarga de hacer la consulta a la base de datos y eliminar el registro correspondiente.
    ClienteDAO.eliminar(cliente)

    #Después de eliminar al cliente, se redirige al usuario a la página de inicio (/).
    #Esto permite actualizar automáticamente la tabla de clientes, mostrando la lista sin el cliente que se acaba de borrar.
    #url_for('inicio') genera la URL correspondiente a la función inicio() de forma segura.
    return redirect(url_for('inicio'))

#Este bloque comprueba si el script está siendo ejecutado directamente (por ejemplo, con python app.py) 
#y no importado como un módulo desde otro archivo. Es una práctica habitual en Python para asegurarse de 
#que cierto código solo se ejecute si el archivo es el punto de entrada principal.
if __name__ == '__main__':

    #Inicia el servidor web de Flask.
    #debug=True activa el modo depuración, lo cual:
        #Muestra mensajes de error detallados si ocurre algún fallo.
        #Recarga automáticamente la aplicación cuando se detectan cambios en el código fuente.
    #Es ideal para desarrollo, pero no debe usarse en PRODUCCIÓN por motivos de seguridad.
    app.run(debug=True)