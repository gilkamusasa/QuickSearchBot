from flask import Flask, render_template, request
from utils import fetch_reply


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    message = request.args.get('msg')
    return str(fetch_reply(message))


if __name__ == "__main__":
    app.run(debug=True)
