class Library:
    def __init__(self, books):
        self.available_books = books
    
    def is_book_available(self, book):
        # If the book is in the list, return True else False
        return book in self.available_books
    
    def get_available_book(self):
        # Returns the list of books
        return self.available_books


books = {
    "Echoes of Eternity",
    "Whispers in the Wind",
    "Sands of Time",
    "The Midnight Garden",
    "Secrets of the Serpent",
    "The Forgotten Realm",
    "Stars Beyond the Sky",
    "Realm of Shadows",
    "The Enchanted Forest",
    "Chronicles of Destiny"
}
book = "Echoes of Eternity"

Answer = Library(books)
result = print(Answer.is_book_available(book))