from flask import Flask
from database import init_db
from routes import Routes

app = Flask(__name__)

def start_app():
  init_db(app)
  Routes(app).init_routes()
  
if __name__ == '__main__':
  start_app()
  app.run(host="0.0.0.0", port=5000, debug=True)