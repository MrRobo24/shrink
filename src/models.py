from database import db

class URL_Map(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  long_url = db.Column(db.String(256), unique=True, nullable=False)
  short_url = db.Column(db.String(256), unique=True, nullable=False)
  
  def __init__(self, long_url, short_url):
      self.long_url = long_url
      self.short_url = short_url