import unittest
from server import app, start_app

class Tests(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    start_app()
    cls.client = app.test_client()
  
  def test_shrink_inserted(self):
    long_url = "www.linkedin.com"
    response = self.client.post("/shrink/" + long_url)
    self.assertEqual(response.status_code, 200)
    
  def test_shrink_invalid_url(self):
    long_url = "123@.linkedin.com"
    response = self.client.post("/shrink/" + long_url)
    self.assertEqual(response.status_code, 400)
    
  def test_load_fetched(self):
    self.test_shrink_inserted()
    short_url = "gj-1sp-0"
    response = self.client.get("/" + short_url)
    self.assertEqual(response.status_code, 302)
    self.assertIn("Location", response.headers)
    self.assertEqual(response.headers["Location"], "http://www.linkedin.com")
  
  def test_load_not_found(self):
    short_url = "random-0"
    response = self.client.get("/" + short_url)
    self.assertEqual(response.status_code, 400)
    
  @classmethod
  def tearDownClass(cls):
    pass
    
if __name__ == '__main__':
    unittest.main()
    