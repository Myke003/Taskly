from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Task

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/home')
def home():
  return '<h1>Taskly</h1>'

@routes.route('/login')
def login():
  return render_template('login.j2')

@routes.route('/register')
def register():
  return render_template('register.j2')

@routes.route('/')
def toDoApp():
  tasks = Task.query.all()
  return render_template('layout.j2', tasks=tasks)


# Crud Routes

@routes.route('/add', methods=['POST'])
def add():
  name = request.form['name']
  new_task = Task(name=name)
  db.session.add(new_task)
  db.session.commit()
  return redirect(url_for('routes.toDoApp'))

@routes.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  task = Task.query.get(id)
  db.session.delete(task)
  db.session.commit()
  return redirect(url_for('routes.toDoApp'))