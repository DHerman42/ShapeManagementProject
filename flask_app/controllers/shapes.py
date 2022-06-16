import os
import datetime
from textwrap import indent
from flask import render_template, redirect, request, session, json
from flask_app.models.shape import Shape
from flask_app import app

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    
    filename = os.path.join(app.static_folder, 'json', 'settings.json')
    f = open(filename)
    data = json.load(f)
    f.close()
    
    #data['factor_date'] = datetime.datetime.now()
    #json.dump(data, open(filename, "w"), indent = 4)

    return render_template('dashboard.html', shapes = Shape.get_all_shapes(), shape_factor = data['shape_factor'])

@app.route('/new')
def newShape():
    if 'user_id' not in session:
        return redirect('/')

    filename = os.path.join(app.static_folder, 'json', 'settings.json')
    f = open(filename)
    data = json.load(f)
    f.close()

    return render_template('newShape.html', shape_factor = data['shape_factor'])

@app.route('/createShape', methods=['POST'])
def new_shape():
    data = {
        'shape_number': request.form['shape_number'],
        'created_at': request.form['created_at'],
        'customer': request.form['customer'],
        'job_name': request.form['job_name'],
        'price': request.form['price'],
        'notes': request.form['notes']
    }

    Shape.create_shape(data)
    return redirect('/dashboard')

@app.route('/delete/<id>')
def remove_shape(id):
    data = {'id': id}
    deleted = Shape.delete_shape(data)
    if deleted:
        return redirect('/dashboard')
    else:
        return redirect('/logout')

@app.route('/edit/<id>')
def edit_shape(id):
    if 'user_id' not in session:
        return redirect('/')

    data = {'id': id}
    shape = Shape.get_shape_by_id(data)

    filename = os.path.join(app.static_folder, 'json', 'settings.json')
    f = open(filename)
    data = json.load(f)
    f.close()
    
    return render_template('editShape.html', shape = shape, shape_factor = data['shape_factor'])

@app.route('/edit', methods=['POST'])
def change_shape():
    data = {
        'id': request.form['id'],
        'shape_number': request.form['shape_number'],
        'customer': request.form['customer'],
        'job_name': request.form['job_name'],
        'price': request.form['price'],
        'notes': request.form['notes'],
    }

    Shape.update_shape(data)
    return redirect('/dashboard')

@app.route('/settings')
def settings():
    filename = os.path.join(app.static_folder, 'json', 'settings.json')
    f = open(filename)
    shape_settings = json.load(f)
    f.close()

    return render_template('settings.html', shape_settings = shape_settings)

@app.route('/updateSettings', methods=['POST'])
def update_settings():
    data = {
        'shape_factor': request.form['shape_factor'],
        'factor_date': datetime.datetime.now()
    }

    filename = os.path.join(app.static_folder, 'json', 'settings.json')
    f = open(filename, "w")
    json.dump(data, f, indent = 4)
    f.close()

    return redirect('/settings')