from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "wiki": "https://en.wikipedia.org/wiki/Nineteen_Eighty-Four"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "wiki": "https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "wiki": "https://en.wikipedia.org/wiki/The_Great_Gatsby"
    }
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add_book', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        new_book = {
            "id": len(books) + 1,
            "title": request.form["title"],
            "author": request.form["author"],
            "year": int(request.form["year"]),
            "wiki": request.form["wiki"]
        }
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('add_book.html')

if __name__ == "__main__":
    app.run(debug=True)
