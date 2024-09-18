import os

from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate  # Importación de la migración

from database import db
from forms import PersonaForm
from models import Persona

# Creación de la aplicación
app = Flask(__name__)

# Configuración de la base de datos
USER_DB = os.getenv('USER_DB')
PASS_DB = os.getenv('PASS_DB')
URL_DB = os.getenv('URL_DB')
NAME_DB = os.getenv('NAME_DB')
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB  # Configuración de la URL de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Configuración de las modificaciones de la base de datos

# Inicialización de la base de datos
db.init_app(app)

# Inicialización de la migración
migrate = Migrate(app, db)

# Configuración de la llave secreta
app.config['SECRET_KEY'] = 'llave_secreta'


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    personas = Persona.query.all()
    total_personas = Persona.query.count()
    app.logger.debug(f'Personas: {personas}')
    app.logger.debug(f'Total Personas: {total_personas}')
    return render_template('index.html', personas=personas, total_personas=total_personas)


@app.route('/ver/<int:id>')
def ver(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona: {persona}')
    return render_template('ver.html', persona=persona)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    persona = Persona()  # Creación de una instancia de la clase Persona
    persona_form = PersonaForm(obj=persona)  # Creación de una instancia de la clase PersonaForm
    if request.method == 'POST':
        if persona_form.validate_on_submit():
            persona_form.populate_obj(persona)  # Inyectar los datos del formulario a la instancia de la clase Persona
            db.session.add(persona)  # Agregar la instancia de la clase Persona a la sesión
            db.session.commit()  # Confirmar la transacción
            return redirect(url_for('index'))

    return render_template('agregar.html', persona_form=persona_form)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    persona = Persona.query.get_or_404(id)
    persona_form = PersonaForm(obj=persona)
    if request.method == 'POST':
        if persona_form.validate_on_submit():
            persona_form.populate_obj(persona)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('editar.html', persona_form=persona_form)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
