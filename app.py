"""
Este archivo controla la aplicación Flask para mi proyecto.
Autor: Sergio Capacho
Fecha: 04/Oct/2024
"""

# Librerías
import os
from flask import Flask
from flask import url_for
from flask import render_template

# Inicialización
mi_app = Flask(__name__)
mi_app.secret_key = "practica"

# Rutas Raíz
@mi_app.route('/')
def inicio():
    return render_template('sitio/index.html')

#Rutas Cursos
@mi_app.route('/cursos')
def cursos():
    return render_template('sitio/02cursos.html') 

# Validación
if __name__ == '__main__':
    mi_app.run(host="127.0.0.1", port=5000, debug=True)

