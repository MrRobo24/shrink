import unittest
import json
from server import app, start_app

class Tests(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    start_app()
    cls.client = app.test_client()
  
  def test_shrink(self):
    long_url = "www.linkedin.com"
    response = self.client.post("/shrink/" + long_url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.text, "gj-1sp-0")
    
  def test_load(self):
    short_url = "gj-1sp-"
    response = self.client.get("/" + short_url)
    self.assertEqual(response.status_code, 302)
    self.assertIn("Location", response.headers)
    self.assertEqual(response.headers["Location"], "http://www.linkedin.com")
    
  @classmethod
  def tearDownClass(cls):
    pass
    
if __name__ == '__main__':
    unittest.main()
    