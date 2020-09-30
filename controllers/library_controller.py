from flask import Flask ,render_template, request, redirect, Blueprint
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all() # NEW
    return render_template("index.html", all_books = books)