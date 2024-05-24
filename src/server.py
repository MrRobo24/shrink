from flask import Flask
from database import init_db
from routes import Routes

def start_app():
  app = Flask(__name__)
  app.config.from_object('config.Config')
  
  init_db(app)
  Routes(app).init_routes()
  return app
  
if __name__ == '__main__':
  app = start_app()
  app.run(debug=True)