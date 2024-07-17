import psycopg2
from flask import Flask, request, redirect, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configuración de conexión a la base de datos
config_db = {
    'database': 'biblioteca3a',
    'user': 'postgres',
    'password': 'bran19',
    'host': 'localhost',
    'port': '5432'
}

@app.route('/')
def index():
    return render_template('base.html')

@app.errorhandler(404)
def  error404(error):
    return render_template('404.htm')


@app.route('/libros')
def libros():
    # Conectar a la base de datos
    conexion = psycopg2.connect(**config_db)

    # Crear un cursor para recorrer las tablas
    cursor = conexion.cursor()
    # Ejecutar una consulta en PostgreSQL
    cursor.execute('''SELECT * FROM libros_view''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libro.html', datos=datos)

@app.route('/autores')
def autores():
    # Conectar a la base de datos
    conexion = psycopg2.connect(**config_db)

    # Crear un cursor para recorrer las tablas
    cursor = conexion.cursor()
    # Ejecutar una consulta en PostgreSQL
    cursor.execute('''SELECT * FROM autores_view''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def paises():
    # Conectar a la base de datos
    conexion = psycopg2.connect(**config_db)

    # Crear un cursor para recorrer las tablas
    cursor = conexion.cursor()
    # Ejecutar una consulta en PostgreSQL
    cursor.execute('''SELECT * FROM país''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('paises.html', datos=datos)

@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    # Conectar a la base de datos
    conexion = psycopg2.connect(**config_db)

    # Crear un cursor para recorrer las tablas
    cursor = conexion.cursor()
    # Borrar el registro con el id_pais seleccionado
    cursor.execute('''SELECT * FROM pais ORDER BY id_pais''')
    conexion.commit()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))

@app.route('/update1_paises/<int:id_pais>', methods=['POST'])
def update1_pais(id_pais):
    # Conectar a la base de datos
    conexion = psycopg2.connect(**config_db)

    # Crear un cursor para recorrer las tablas
    cursor = conexion.cursor()
    # Recuperar el registro del id_pais seleccionado
    cursor.execute('''SELECT * FROM país WHERE id_pais=%s''', (id_pais,))
    datos = cursor.fetchone()  # Usar fetchone() ya que esperamos solo una fila
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('editar_pais.html', datos=datos)

@app.route('/update2_pais/<int:id_pais>', methods=['POST'])
def update2_pais(id_pais):
    # Conectar a la base de datos
    conexion = psycopg2.connect(**config_db)

    # Recuperar datos del formulario
    nombre = request.form['nombre']

    # Crear un cursor para recorrer las tablas
    cursor = conexion.cursor()
    # Actualizar el registro con el id_pais seleccionado
    cursor.execute('''UPDATE país SET nombre=%s WHERE id_pais=%s''', (nombre, id_pais))
    conexion.commit()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))