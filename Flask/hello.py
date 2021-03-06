from flask import Flask, request, render_template, url_for, redirect
import json

# Ejecutar en consola ming64
# export FLASK_ENV=development
# FLASK_APP=hello.py flask run

app = Flask(__name__)


# http://localhost:5000/Nestor
@app.route('/')
@app.route('/<nombre>')
@app.route('/<nombre>/<apellidos>')
def hello(nombre="Invitado", apellidos=""):
    data = {
        'nombre': nombre,
        'apellidos': apellidos
    }

    if request.cookies.get('data'):
        cookieData = json.loads(request.cookies.get('data'))
        if cookieData.get('nombre'):
            data['nombre'] = cookieData.get('nombre')

    return render_template('index.html', **data)


@app.route("/images")
def hello_image():
    return "Hello Images"


@app.route("/hola_mundo")
def hola_mundo():
    return "hola_mundo"


@app.route("/multiplicar")
def multiplicar():
    return "multiplicar2s"


# http://localhost:5000/sumar?num1=3&num2=2323
@app.route("/sumar")
def sumar(num1=0, num2=0):
    try:
        num1 = int(request.args.get('num1', num1))
    except ValueError:
        num1 = 0

    try:
        num2 = int(request.args.get('num2', num2))
    except ValueError:
        num2 = 0

    result = num1 + num2

    return "{} + {} = {}".format(num1, num2, result)


# http://localhost:5000/sumar2/455/555
@app.route("/sumar2/<int:num1>/<int:num2>")
@app.route("/sumar2/<float:num1>/<float:num2>")
def sumar2(num1=0, num2=0):
    result = num1 + num2

    return "{} + {} = {}".format(num1, num2, result)


# http://localhost:5000/sumar3/455/555
@app.route("/sumar3/<int:num1>/<int:num2>")
@app.route("/sumar3/<float:num1>/<float:num2>")
def sumar3(num1=0, num2=0):
    resultado = num1 + num2
    return """
<!doctype html>
<html>
    <head>
        <title>Suma</title>
    </head> 
    <body>
        <h1>{} + {} = {}</h1>
    </body>
</html>
    """.format(num1, num2, resultado).strip()


# http://localhost:5000/sumar4/455/555
@app.route("/sumar4/<int:num1>/<int:num2>")
@app.route("/sumar4/<float:num1>/<float:num2>")
def sumar4(num1=0, num2=0):
    resultado = num1 + num2
    data = {
        'num1': num1,
        'num2': num2,
        'resultado': resultado
    }
    return render_template("suma.html", **data)


# http://localhost:5000/contacto/
@app.route("/contacto")
def contacto(nombre='', email='', comentario=''):
    data = {
        'nombre': nombre,
        'email': email,
        'comentario': comentario
    }
    return render_template("contacto.html", **data)


# http://localhost:5000/enviar/
@app.route("/enviar", methods=['POST'])
def enviar():
    response = redirect(url_for("hello"))
    response.set_cookie('data', json.dumps(dict(request.form.items())))
    return response


if __name__ == "__main___":
    app.run(debug=True)
