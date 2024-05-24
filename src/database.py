from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///url_map.sqlite3"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.init_app(app)
  
  with app.app_context():
    db.create_all()  

def insert_db(model):
  db.session.add(model)
  db.session.commit()

def find_one_db(model, short_url):
  return db.session.query(model).filter_by(short_url=short_url).one_or_none()
