from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    greeting = os.getenv("GREETING", "Hello, World!")
    return f"<h1>{greeting}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
