from flask import Flask,render_template
name = Flask(__name__)

@app.route("/")
def home(self):
    return render_template(index.html)

@app.route("/", methods=("GET", "POST"))
def login(self):
    if request method == "POST"
    return render_template(login.html)

@app.route("/")
def profile(self):
    return render_template(profile.html)



