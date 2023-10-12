import os
from flask import Flask, render_template , request, Response

app = Flask(__name__)

@app.route('/')
def hello():
    color = 'blue'
    return render_template('hello.html', color=color)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)