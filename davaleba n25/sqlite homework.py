import sqlite3

conn = sqlite3.connect('book_db.sqlite')
cursor = conn.cursor()

queries = [
    ("All fields from the book table", "SELECT * FROM book"),
    ("Titles of books authored by Rowling", "SELECT title FROM book WHERE author LIKE '%Rowling%'"),
    ("Titles of books with price < 20", "SELECT title FROM book WHERE price < 20"),
    ("All books sorted by title (ascending)", "SELECT * FROM book ORDER BY title ASC"),
    ("Titles of books with more than 100 pages", "SELECT title FROM book WHERE pages > 100"),
    ("Books published in 2018", "SELECT * FROM book WHERE year = 2018"),
    ("Titles of books not published in 2018", "SELECT title FROM book WHERE year != 2018"),
    ("Maximum price among all books", "SELECT MAX(price) AS max_price FROM book"),
    ("Minimum number of pages among all books", "SELECT MIN(pages) AS min_pages FROM book")
]

for description, query in queries:
    print(description)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()
