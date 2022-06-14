from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app import app

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def new_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'user_name': request.form['user_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.register(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route("/login", methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }

    user_in_db = User.validate_login(data)

    if not user_in_db:
        return redirect('/')
    else:
        session['user_id'] = user_in_db['id']
    return redirect('/dashboard')