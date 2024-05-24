from handlers import Handler

class Routes():
  def __init__(self, app) -> None:
    self.app = app
    
  def init_routes(self):
    handler = Handler()
    @self.app.route("/shrink/<long_url>", methods=["POST"])
    def shrink(long_url):
      return handler.handleShrinkCall(long_url)

    @self.app.route("/<short_url>", methods=["GET"])
    def load(short_url):
      print(short_url)
      return handler.handleLoadCall(short_url)