from flask import (Flask, redirect, url_for,
                   render_template, request, session)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    name = request.args.get("name", "Name not found")
    surname = request.args.get("surname", "Surname not found")
    return render_template("index.html",
                           name=name,
                           surname=surname)

@app.route('/profile')
def profile():
    name = request.args.get("name", "Jasurbeki")
    surname = request.args.get("surname", "Surname not found")
    return render_template("profile.html",
                           name=name,
                           surname=surname)


@app.route('/login')
def login():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        session['user'] = user_email
        session['password'] = user_password
        return redirect(url_for("profile"))
    else:
        return render_template("login.html")

# @app.route('/about')
# def about():
#     return '<p>This is about us page</p>'
#
#
# @app.route('/<name>/<surname>/<int:age>/')
# def profile(name, surname, age):
#     subjects = ["ქართული", "მათემატიკა", "ინგლისური"]
#     return render_template("user.html",
#                            user_name=name,
#                            user_surname=surname,
#                            user_age=age,
#                            user_subjects=subjects)
#
#
# @app.route('/admin')
# def admin():
#     return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
