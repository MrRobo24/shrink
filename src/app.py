from flask import Flask, redirect

app = Flask(__name__)

@app.route("/shrink/<long_url>")
def shrink(long_url):
  return long_url

@app.route("/<short_url>")
def load(short_url):
  return redirect("http://www." + short_url)

if __name__ == '__main__':
  app.run(debug=True)