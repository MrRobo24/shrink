from flask import Flask, redirect
# from database import init_db, insert_db, find_one_db
# from models.url_map import URL_Map
from flask_sqlalchemy import SQLAlchemy
import hashlib
import base64

app = Flask(__name__)

#database

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///url_map.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


#models
class URL_Map(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  long_url = db.Column(db.String(256), unique=True, nullable=False)
  short_url = db.Column(db.String(256), unique=True, nullable=False)
  
  def __init__(self, long_url, short_url):
      self.long_url = long_url
      self.short_url = short_url

with app.app_context():
  db.create_all()
  
def find_one_db(model, short_url) -> URL_Map:
  return db.session.query(model).filter_by(short_url=short_url).one_or_none()
  
def insert_db(model):
  db.session.add(model)
  db.session.commit()
  
  
#utils
def generate_short_url(long_url):
    # Create a SHA-256 hash of the long URL
    sha256_hash = hashlib.sha256(long_url.encode()).digest()
    
    # Encode the hash using Base64 and take the first 6 characters
    short_url = base64.urlsafe_b64encode(sha256_hash).decode()[:6]
    return short_url

#routes
@app.route("/shrink/<long_url>", methods=["POST"])
def shrink(long_url):
  short_url = generate_short_url(long_url)
  maybe_url_map = find_one_db(URL_Map, short_url)
  if maybe_url_map != None:
    short_url = maybe_url_map.short_url
  else:  
    url_map = URL_Map(long_url=long_url, short_url=short_url)
    try:
      insert_db(url_map)
    except:
      return "URL insertion failed"

  return short_url

@app.route("/<short_url>", methods=["GET"])
def load(short_url):
  url_map = None
  try:
    url_map = find_one_db(URL_Map, short_url)
  except:
    return "URL fetch failed"
  
  if url_map != None:
    return redirect("http://" + url_map.long_url)
  else:
    return "No URL record found"
  

if __name__ == '__main__':
  app.run(debug=True)