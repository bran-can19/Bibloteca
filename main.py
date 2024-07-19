from flask.templating import _render
import psycopg2
from flask import Flask, request, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField,SubmitField
import db
from forms import Librosform

app = Flask(__name__)
bootstrap = Bootstrap(app)


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SUPER SECRETO'

@app.route('/')
def index():
    return render_template('base.html')

@app.errorhandler(404)
def  error404(error):
    return render_template('404.htm')

@app.route('/libros')
def libros():
    conn = db.conetar()

    # Crear un cursor para recorrer las tablas
    cursor = conn.cursor()
    # Ejecutar una consulta en PostgreSQL
    cursor.execute('''SELECT * FROM libros_view Order by id_libro''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template(('libros.html'), datos=datos)


@app.route('/insertar_libro', methods=['GET','POST'])
def insertar_libro():
    form= Librosform()
    if form.validate_on_submit():
        #si se dio click en el boton del form y no faltan datos.
        #se  recupera la imformacion que el user escribio en el form.
        titulo=form.titulo.data
        fk_autor=form.fk_autor.data
        fk_editorial=form.fk_editorial.data
        edicion=form.edicion.data
        #Insertar los datos
        conn= db.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO libro (titulo, fk_autor, fk_editorial, edicion)
                    VALUES (%s, %s, %s, %s)
'''(titulo, fk_autor, fk_editorial, edicion))
        conn.commit()
        cursor.close()
        db.desconectar()
        return redirect(url_for('libros'))
    end if
    return render_template('insertar_libro.html', form=form)












@app.route('/autores')
def autores():
    conn = db.conetar()

    # Crear un cursor para recorrer las tablas
    cursor = conn.cursor()
    # Ejecutar una consulta en PostgreSQL
    cursor.execute('''SELECT * FROM autores_view''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def paises():
    # Conectar a la base de datos
    conn = db.conetar()
    # Crear un cursor para recorrer las tablas
    cursor = conn.cursor()
    # Ejecutar una consulta en PostgreSQL
    cursor.execute('''SELECT * FROM pais''')
    # Recuperar la información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('pais.html', datos=datos)

@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    conn = db.conetar()

    # Crear un cursor para recorrer las tablas
    cursor = conn.cursor()
    # Borrar el registro con el id_pais seleccionado
    cursor.execute('''SELECT * FROM pais ORDER BY id_pais''')
    conn.commit()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))

@app.route('/update1_paises/<int:id_pais>', methods=['POST'])
def update1_pais(id_pais):
    conn = db.conetar()

    # Crear un cursor para recorrer las tablas
    cursor = conn.cursor()
    # Recuperar el registro del id_pais seleccionado
    cursor.execute('''SELECT * FROM pais WHERE id_pais=%s''', (id_pais,))
    datos = cursor.fetchall()  # Usar fetchone() ya que esperamos solo una fila
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('editar_pais.html', datos=datos)

@app.route('/update2_pais/<int:id_pais>', methods=['POST'])
def update2_pais(id_pais):
    nombre= request.form['nombre']
    conn = db.conetar()

    cursor = conn.cursor()
    cursor.execute('''UPDATE pais SET nombre=%s WHERE id_pais=%s''', (nombre, id_pais))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))