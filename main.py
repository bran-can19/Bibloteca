import psycopg2
from flask import Flask,request,redirect,render_template,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField,StringField,SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/libros')
def libros():
    #conectar con la BD
    conexion= psycopg2.connect(
        database= "Biblioteca3a",
        user="postgres",
        password="cris20",
        host="localhost",
        port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)
    cursor= conexion.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM libros_view''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():
    #conectar con la BD
    conexion= psycopg2.connect(
        database= "Biblioteca3a",
        user="postgres",
        password="cris20",
        host="localhost",
        port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)
    cursor= conexion.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM autores_view''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def paises():
    #conectar con la BD
    conexion= psycopg2.connect(
        database= "Biblioteca3a",
        user="postgres",
        password="cris20",
        host="localhost",
        port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)
    cursor= conexion.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM país''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    conexion.close()
    return render_template('paises.html', datos=datos)

@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    #conectar con la BD
    conexion= psycopg2.connect(
        database= "Biblioteca3a",
        user="postgres",
        password="cris20",
        host="localhost",
        port="5432"
    )
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conexion.cursor()
    #Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM país WHERE id_pais=%s''',
                    (id_pais,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))

@app.route('/update1_pais/<int:id_pais>', methods=[ 'POST'])
def update1_pais(id_pais):
    #conectar con la BD
    conexion= psycopg2.connect(
        database= "Biblioteca3a",
        user="postgres",
        password="cris20",
        host="localhost",
        port="5432"
    )
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conexion.cursor()
    #recuperar el registro del id_pais seleccionado
    cursor.execute( '''SELECT*FROM país WHERE id_pais=%s''' ,
                    (id_pais,))
    datos=cursor.fetchall()
    id_pais=request.form['id_pais']
    nombre=request.form['nombre']
    datos={
         'id_pais':id_pais,
         'nombre':nombre
    }
    cursor.close()
    conexion.close()
    return render_template ('editar_pais.html', datos=datos)