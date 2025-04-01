from flask import Flask
from app.routes import routes
from app.models import db

app = Flask(__name__, static_folder='app/static', template_folder='app/templates')
app.register_blueprint(routes)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/taskly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':

  with app.app_context():
    db.create_all()

  app.run(debug=True)