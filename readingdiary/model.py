from datetime import datetime
from xml.dom.xmlbuilder import Options


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
       return f"{self.date} - page {self.page}: {self.text}"

class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int, rating: int, notes: list[Note]):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        self.notes.append(Note(text, page, date))
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD or Book.BAD):
            return False
        self.rating = rating
        return True
    def get_notes_of_pages(self, page: int) -> list[Note]:
        return [note for note in self.notes if note.page == page]
    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1
        count_pages = {}
        for note in self.notes:
            count_pages[note.page]= count_pages.get(note.page, 0) + 1

        return max(count_pages, key=count_pages.get)
    def __str__(self) -> str:
        rating_str = {
            Book.EXCELLENT: "excellent",
            Book.GOOD: "good",
            Book.BAD: "bad",
            Book.UNRATED: "unrated"
        }[self.rating]

        return (f"ISBN: {self.isbn}"
        f"Title: {self.title}"
        f"Author: {self.author}"
        f"Pages: {self.pages}"
        f"Rating: {rating_str}")

class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn in self.books:
            return False
        self.books[isbn] = Book(isbn, title, author, pages)
        return True

