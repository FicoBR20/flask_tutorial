'''
La Interfaz de Pasarela del Servidor Web, o Web Server Gateway Interface en inglés (WSGI), 
es una interfaz estándar entre el servidor web y aplicaciones web escritas en Python. 
Con una interfaz estándar es más sencillo usar una aplicación que soporte WSGI 
con diferentes servidores web.

NOTAS;
    // app esta en desarrollo NO en produccion. facilita el probarla
    export FLASK_APP=app.py
    export FLASK_ENV=development 
    flask run

    ! mas ENTER se genera el encabezado para un HTML doc.
    
    La funcion render_template nos permite retornar desde una funcion, un archivo htmil.

    linea 40 : Ejemplo de como pasar una variable desde python hacia htmol, aprovecha el motor jinja
    El motor jinja toma un html y lo reprograma con su propia sintaxis y semantica.

 
'''

from flask import Flask, render_template, request

app = Flask(__name__)

'''

@app.route("/home") # esta ruta tambien nos entrega "hola papito Dios", una funcion con dos rutas o decoradores+


@app.route("/") #decorador o rutas;implementa la raiz del servidor;
# por ejemplo http://127.0.0.1:5000/, entonces el ultimo "/" es nuestra raiz
def index():
   # return "hola papito Diosito Lindo y Puro !"
   return render_template("index.html") # debe estar en el folder denominado templates el framework lo exige

@app.route("/contacto") # corresponde a la ruta http://127.0.0.1:5000/contacto, osea raiz/contacto.
def contacto():
    return("<h1>es tu contacto</h1>") #entrega una etiqueta html de tipo h1 

@app.route("/hola/<string:nombre>") # pasar un parametro a la ruta, en este caso "nombre"
def hola(nombre):
    return f"<h1>hola {nombre}</h1>"

@app.route("/exm1") # esta ruta nos recrea como lograr pasar variables a un HTML desde python
def introducir():
    my_name = " Univalle "
    return render_template("index.html", algun_nombre = my_name) # se pasa al html algun_nombre

@app.route("/exm2") # ejemplo de hacer un if else con jinja
def useifel():
    num=1
    return render_template("index.html", some_number = num) # se pasa al html some_number

@app.route("/exm3") # ejemplo de for con jinja
def uselist():
    mylist =[1,2,3,4,5, "jose"]
    return render_template("index.html", someList = mylist)

@app.route("/saludo")
def elsaludo():
    return render_template("saludo.html")

@app.route("/hijo")
def mihijo():
    return render_template("hijo.html")

'''

@app.route("/") #practica con formularios P1
def ffuncion():
    return render_template("formu.html")

'''
por default cada decorador o puerto tiene el metodo "GET", o sea siempre se configura para obtener alguna informacionñ
asi que si nesecitamos que un puerto cambie de metodo, debemos especificarlo en el constructor.

'''

@app.route("/mycontact", methods=["POST"])# POST usa metodo request que informa sobre el origen de la info
def contact_func():
    '''
    se crea la variable "algun_nombre" y se le asigna el input name de formu.html;
    luego se retorna una nueva variable "contac_nombre", la cual se renderiza en el documento
    contacto.html, a esta variable se le asigna la variable "algun_nombre"
    '''
    algun_nombre = request.form.get("El_nombre")# se crea variable y se "trae" (request) y asigna el name input
    return render_template("contacto.html", contact_nombre = algun_nombre)# crear "contact_nombre" y asignar para render

# como accesar archivo html





if __name__== "__main__": # nos permite que la app este en modo de prueba "debug" sin cerrar servidor.
    app.run(debug=True)
