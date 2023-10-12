import os
from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def show_color():
    color = 'blue'
    return render_template('hello.html', color=color)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)