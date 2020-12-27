from flask import Flask, render_template

from lib.settings import SETTINGS

app = Flask(__name__)


@app.route("/")
def index():
    # return the rendered template
    return render_template("index.html", host=SETTINGS.server_ip)


def start_web_server():
    app.run(SETTINGS.server_ip, SETTINGS.web_port)
