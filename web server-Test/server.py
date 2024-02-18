from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def hello_1():
    return "<p>This is my website</p>"

@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('./index.html', name = username, post_id=post_id)

@app.route("/blog/dogs")
def blog():
    return "<p>This is my dog</p>"

@app.route("/about.html")
def about():
    return render_template('about.html')