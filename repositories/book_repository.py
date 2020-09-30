from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, genre, year) VALUES (%s,%s, %s) RETURNING *"
    values = [book.title, book.genre, book.year]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        book = Book(row['title'], row['genre'], row['year'], row['id'])
        books.append(book)
    return books

