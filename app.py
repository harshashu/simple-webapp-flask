import os
from flask import Flask
app = Flask(__name__)
color = "red" 

@app.route("/")
def main():
    #return 'Hello'
        return 'hello.html'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
