class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def get_books(self):
        return self.books
        
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, author=None, title=None):
        book_list = []
        
        for book in self.books:
            if author and title:
                if author == book.author and title.lower() in book.title.lower():
                    book_list.append(book)
            elif author:
                if author == book.author:
                    book_list.append(book)
            elif title:
                if title.lower() in book.title.lower():
                    book_list.append(book)
        
        return book_list

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.books.append(self)