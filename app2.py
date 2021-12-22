# La clase Flask proporciona la función redirect () que redirige al usuario a alguna URL especificada con el código de estado especificado.

# Veamos el siguiente ejemplo donde el usuario es redirigido a la página de éxito con el  inicio de sesión exitoso (usuario = cualquier correo, clave = 123) de lo contrario; el usuario vuelve a esta página únicamente.

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home ():  
    return render_template("home.html")  
 
@app.route('/login')  
def login():  
    return render_template("login.html");  
 
@app.route('/validar', methods = ["POST"])  
def validar():  
    if request.method == 'POST' and request.form['pass'] == '123':  
        return redirect(url_for("exito"))  
    return redirect(url_for("login"))  
 
@app.route('/exito')  
def exito():  
    return "logueado correctamente!"  
  
if __name__ == '__main__':  
    app.run(debug = True)  