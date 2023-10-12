from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])


@app.route("/")
def main():
    # return 'Hello'
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[COLOR])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
