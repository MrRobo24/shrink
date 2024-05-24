from flask import redirect
from models import URL_Map
from utils import generate_short_url, incr_suff_on_collision
from database import insert_db, find_one_db
  
class Handler():
  def handleLoadCall(self, short_url):
    url_map = find_one_db(URL_Map, short_url)
    return redirect("http://" + url_map.long_url) if url_map != None else "URL fetch failed"
    
  def handleShrinkCall(self, long_url):
    short_url = generate_short_url(long_url)
    old_url_map: URL_Map = find_one_db(URL_Map, short_url)
    if old_url_map != None:
      if old_url_map.long_url == long_url:
        return old_url_map.short_url
      else:
        short_url = incr_suff_on_collision(short_url)
    else:  
      url_map = URL_Map(long_url=long_url, short_url=short_url)
      return "URL insertion failed" if not insert_db(url_map) else short_url