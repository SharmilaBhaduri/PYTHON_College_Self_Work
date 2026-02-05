class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

books = []

print("Enter details for each book (title, author, price), one book per line. Enter 'done' to finish.")

while True:

    entry = input("Enter book details (title, author, price): ")

    if entry.lower() == 'done':
        break

    title, author, price = entry.split(',')
    books.append(Book(title.strip(), author.strip(), float(price.strip())))

sorted_books_by_title = sorted(books, key=lambda x: x.title)

print("Sorted books by title:")

for book in sorted_books_by_title:
    print(f"{book.title} by {book.author}, Price: ${book.price}")

sorted_books_by_price = sorted(books, key=lambda x: x.price)

print("\nSorted books by price:")

for book in sorted_books_by_price:
    print(f"{book.title} by {book.author}, Price: ${book.price}")
