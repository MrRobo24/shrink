from flask import redirect
from models import URL_Map
from database import find_one_db, insert_db
from utils import generate_short_url
  
def handleLoadCall(short_url):
  url_map = None
  try:
    url_map = find_one_db(URL_Map, short_url)
  except :
    return "URL fetch failed"
  
  if url_map != None:
    return redirect("http://" + url_map.long_url)
  else:
    return "No URL record found"
  
def handleShrinkCall(long_url):
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