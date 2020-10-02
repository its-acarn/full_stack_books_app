import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("Kurt", "Vonnegut")
author_repository.save(author1)
author2 = Author("Brandon", "Sanderson")
author_repository.save(author2)

book1 = Book("Cats Cradle", "satire", 1963)
book_repository.save(book1)
book2 = Book("Breakfast of Champions", "satire", 1973)
book_repository.save(book2)
book3 = Book("The Way of Kings", "High Fantasy", 2010)
book_repository.save(book3)
book4 = Book("Words of Radiance", "High Fantasy", 2014)
book_repository.save(book4)

pdb.set_trace()
