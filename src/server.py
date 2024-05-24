from flask import Flask
from database import init_db
from routes import init_routes

def start_app(app):
  init_db(app)
  init_routes(app)

if __name__ == '__main__':
  app = Flask(__name__)
  start_app(app)
  app.run(debug=True)