# Construcción de URL

# La función url_for () se utiliza para crear una URL a la función específica de forma 
# dinámica. El primer argumento es el nombre de la función especificada, y luego podemos 
# pasar cualquier número de argumento de palabra clave correspondiente a la parte 
# variable de la URL.

# Esta función es útil en el sentido de que podemos evitar la codificación rígida de las 
# URL en las plantillas construyéndolas dinámicamente utilizando esta función.


# El script siguiente simula el sistema de gestión de la biblioteca que pueden utilizar 
# los tres tipos de usuarios, es decir, administrador, bibliotecario y estudiante. Hay 
# una función específica llamada usuario () que reconoce al usuario y lo redirige a la 
# función exacta que contiene la implementación de esta función en particular.

# Por ejemplo: 
# La URL http: // localhost: 5000 / usuario / admin se redirige a la 
# URL http: // localhost: 5000 / admin 

# La URL localhost: 5000 / usuario / biblioteca, se redirige a la 
# URL http: // localhost: 5000 / biblioteca

# La URL http: // localhost: 5000 / usuario / estudiante se redirige a la 
# URL http: // localhost / estudiante.

# Beneficios de la creación de URL dinámicas
# Evita la codificación rígida de las URL.

# Podemos cambiar las URL dinámicamente en lugar de recordar las URL codificadas que se 
# cambiaron manualmente.

# La construcción de URL maneja el escape de caracteres especiales y datos Unicode de 
# forma transparente.

# Las rutas generadas son siempre absolutas, evitando comportamientos inesperados de 
# rutas relativas en los navegadores.

# Si su aplicación se coloca fuera de la raíz de la URL, por ejemplo, en / myapplication 
# en lugar de /, url_for () lo maneja correctamente por usted.

from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/biblioteca')  
def biblioteca():  
    return 'biblioteca'  
  
@app.route('/estudiante')  
def estudiante():  
    return 'estudiante'  
  
@app.route('/usuario/<nombre>')  
def usuario(nombre):  
    if nombre == 'admin':  
        return redirect(url_for('admin'))  
    if nombre == 'biblioteca':  
        return redirect(url_for('biblioteca'))  
    if nombre == 'estudiante':  
        return redirect(url_for('estudiante'))



if __name__ =='__main__':  
    app.run(debug = True)  