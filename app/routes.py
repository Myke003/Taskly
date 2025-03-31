from flask import Blueprint, render_template

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
  return render_template('layout.j2')


# Crud Routes

@routes.route('/add')
def add():
  return 'add task'

@routes.route('/update')
def update():
  return 'update'

@routes.route('/delete')
def delete():
  return 'delete'