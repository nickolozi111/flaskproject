import sqlite3

conn = sqlite3.connect("titanic.sqlite")
cursor = conn.cursor()

result = (SELECT * FROM titanic.sqlite)
# cursor.execute('''
# CREATE TABLE books(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# title VARCHAR(50),
# author VARCHAR(100),
# price FLOAT
# );
# ''')
# b_title = "animal farm"
# b_author = "george orwell"
# b_price = 10.5
#
# book1 = ("1984","george orwell", 10.6)
# cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (book1))
#
# book_list = [
#             ('The Book Thief', 'Markus Zusak', 17 ),
#             ('Animal Farm', 'George Orwell', 13 ),
#             ('The Hunger Games', 'Suzanne Collins', 17 ),
#             ('Harry Potter and the Prisoner of Azkaban', 'Rowling',  25),
#             ('Harry Potter and the Goblet of Fire', 'Rowling', 24 ),
#             ('გამზრდელი', 'აკაკი წერეთელი', 8),
#             ('ჩემი თავგადასავალი', 'აკაკი წერეთელი', 8),
#             ('განდეგილი', 'ილია ჭავჭავაძე', 10 ),
#             ('ვეფხისტყაოსანი', 'შოთა რუსთაველი', 29)
#         ]
# cursor.executemany('INSERT INTO books (title, author, price) VALUES (?,?,?)', book_list)
#
# # cursor.execute("INSERT INTO books (title, author, price) VALUES ('Hamlet', 'William Shakespeare', 10.5);")
# conn.commit()
# cursor.execute("SELECT * FROM books")
# record = cursor.fetchone()
# print("Title =", record[1])
# records = cursor.fetchall()
# for record in records:
#     print(record)
# conn.close()

















