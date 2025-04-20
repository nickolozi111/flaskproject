from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/about')
def about():
    return "About"

@app.route('/<name>/<surname>/<int:age>')
def profile(name, surname, age):
    return render_template("user.html", surname=surname, name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
