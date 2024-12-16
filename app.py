'''
NOTA IMPORTANTE: En la rama dtt2 desarrollaremos el tutorial 2

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

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")






if __name__== "__main__": # nos permite que la app este en modo de prueba "debug" sin cerrar servidor.
    app.run(debug=True)
