from flask import Flask, render_template, request, redirect, url_for, flash,session
from config import config
from flask_mysqldb import MySQL
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from Models.Entities.ModelUser import ModelUser
from Models.Entities.ModelUser import User
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf=CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app) 

@login_manager_app.user_loader
def load_userr(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('register'))


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        correo = request.form['correo']
        password = request.form['password']

        if not username or not correo or not password:
            flash('Todos los campos son obligatorios.')
            return redirect(url_for('register'))

        user = User(None, username, correo, password)
        result = ModelUser.register(db, user)

        if result == "OK":
            flash('¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect(url_for('login'))
        else:
            flash(result)
            return redirect(url_for('register'))

    return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        print(f"Correo ingresado: {correo}")
        print(f"Contraseña ingresada: {password}")

        if not correo or not password:
            flash("Todos los campos son obligatorios.")
            return redirect(url_for('login'))

        user = User(None, None, correo, password)
        logged_user = ModelUser.login(db, user)

        print(f"Usuario recuperado: {logged_user}")

        if logged_user:
            session['user_id'] = logged_user.id
            session['username'] = logged_user.username
            flash("Sesión iniciada correctamente.")
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            flash("Correo o contraseña incorrectos.")
            return redirect(url_for('login'))

    return render_template('auth/login.html')

@app.route('/home')
@login_required
def home():
    return render_template('auth/home.html')

@app.route('/principal')
@login_required
def principal():
    return render_template('auth/main.html')

def status_401(error):
    return redirect(url_for('register'))

def status_404(error):
    return "<h1>Página no encontrada.</h1>", 404


if __name__ =='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()