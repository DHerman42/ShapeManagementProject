from flask import render_template, redirect, request, session
from flask_app.models.shape import Shape
from flask_app import app

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dashboard.html', shapes = Shape.get_all_shapes())

@app.route('/new')
def newShape():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('newShape.html')

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