from flask import (Flask, redirect, url_for,
                   render_template, request, session)

app = Flask(__name__)

@app.route("/profile")
def home():
    return render_template()

@app.route("/")
def profile():
    if user in session
        user = session(user)
        return user
    else redirect(url_for)



if __name__ == "__main__":
    app.run(debug=True)
