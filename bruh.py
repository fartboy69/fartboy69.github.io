from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello! This is written in my py file. <h1>t</h1>"

if __name__ == "__main__":
    app.run()