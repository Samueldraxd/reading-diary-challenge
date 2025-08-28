from datetime import datetime


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text = text
        self.page = page
        self.date = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    # Constantes
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = Book.UNRATED        # inicia unrated
        self.notes: list[Note] = []       # lista vacía

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        # False si la página no existe
        if page > self.pages:
            return False
        self.notes.append(Note(text, page, date))
        return True

    def set_rating(self, rating: int) -> bool:
        # Acepta solo EXCELLENT, GOOD o BAD
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        # Debe devolver lista (vacía si no hay)
        return [n for n in self.notes if n.page == page]

    def page_with_most_notes(self) -> int:
        # -1 si no hay notas
        if not self.notes:
            return -1
        counts: dict[int, int] = {}
        for n in self.notes:
            counts[n.page] = counts.get(n.page, 0) + 1
        return max(counts, key=counts.get)

    def __str__(self) -> str:
        # Metodo str
        rating_str = {
            Book.EXCELLENT: "excellent",
            Book.GOOD: "good",
            Book.BAD: "bad",
            Book.UNRATED: "unrated",
        }[self.rating]
        return (f"ISBN: {self.isbn}\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Pages: {self.pages}\n"
                f"Rating: {rating_str}")


class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        # Falso si ya existe ISBN
        if isbn in self.books:
            return False
        self.books[isbn] = Book(isbn, title, author, pages)
        return True

    def search_by_isbn(self, isbn: str) -> Book | None:
        return self.books.get(isbn)

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.add_note(text, page, date)

    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)

    def book_with_most_notes(self) -> Book | None:
        # nada si no hay libros o todos tienen 0 notas
        if not self.books:
            return None
        max_book: Book | None = None
        max_count = 0
        for book in self.books.values():
            c = len(book.notes)
            if c > max_count:
                max_count = c
                max_book = book
        return max_book if max_count > 0 else None
