#PROXIMAMENTE SE AÑADIRAN COMENTARIOS EXPLICANDO EL CÓDIGO
from flask import Flask, redirect, render_template, url_for
from cliente_forma import ClienteForma
from cliente import Cliente
from cliente_dao import ClienteDAO

app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave'

titulo_app = 'Zona Fit (GYM)'

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html')

def inicio():
    app.logger.debug('Entramos al path de inicio /')
    #recuperar clientes de la BBDD
    clientes_db = ClienteDAO.seleccionar()
    cliente_forma = ClienteForma()
    #crear objeto de formulario cliente vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    #creamos los objetos de cliente, inicalmente vacios
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)

    if cliente_forma.validate_on_submit():
        #llenamos el objeto cliente con los valores del formulario
        cliente_forma.populate_obj(cliente)

        if not cliente.id:
            #guardamos el nuevo cliente en la BBDD
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)

    #Redireccionar página de inicio
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    #recuperar listado de clientes
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)