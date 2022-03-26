from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welocme to the Dockerized Flask App</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000",debug=True)