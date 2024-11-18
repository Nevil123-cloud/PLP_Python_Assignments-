class Book:
    def __init__(self, title, author, pages):
        self.title = title  # Attribute
        self.author = author  # Attribute
        self.pages = pages  # Attribute

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")

book = Book("Things Fall Apart", "Chinua Achebe", 209)
print(book.title)
book.read()      
