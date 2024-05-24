from handlers import handleShrinkCall, handleLoadCall

def init_routes(app):
  @app.route("/shrink/<long_url>", methods=["POST"])
  def shrink(long_url):
    return handleShrinkCall(long_url)

  @app.route("/<short_url>", methods=["GET"])
  def load(short_url):
    print(short_url)
    return handleLoadCall(short_url)