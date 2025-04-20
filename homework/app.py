from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    home_text = "Welcome to the Home Page!"
    items = ["Apple", "Banana", "Cherry"]
    return render_template('home.html', home_text=home_text, items=items)

@app.route('/about')
def about():
    about_text = "This is the About Page where we talk about ourselves."
    return render_template('about.html', about_text=about_text)

@app.route('/third_page')
def third_page():
    theme = "This is a dynamic page about Tech."
    show_content = True  # Conditional content
    return render_template('third_page.html', theme=theme, show_content=show_content)

if __name__ == "__main__":
    app.run(debug=True)
