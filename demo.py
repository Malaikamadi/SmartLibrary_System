# demo.py
from operations import BOOKS, MEMBERS, CATEGORIES
from operations import add_book, add_member, borrow_book, return_book
from operations import update_book, update_member, delete_book, delete_member, search_books


def print_state():
    print("\nCurrent Books:")
    for isbn, book in BOOKS.items():
        print(f"{isbn}: {book}")
    print("\nCurrent Members:")
    for member in MEMBERS:
        print(member)
    print("\n" + "-" * 50 + "\n")


def main():
    print("Welcome to Mini Library System")
    print(f"Book categories: {CATEGORIES}\n")

    # ---- Add Books ----
    add_book("101", "Python Basics", "John Doe", "Non-Fiction", 3)
    add_book("102", "Space World", "Mary Jay", "Sci-Fi", 2)
    add_book("103", "Love and Life", "James Ray", "Romance", 1)
    add_book("104", "Mystery Night", "Anne Brown", "Mystery", 4)
    add_book("105", "Life Story", "Sam Green", "Biography", 2)

    # ---- Add Members ----
    add_member("M001", "Alice", "alice@mail.com")
    add_member("M002", "Bob", "bob@mail.com")
    add_member("M003", "Charlie", "charlie@mail.com")

    print("Initial state:")
    print_state()

    # ---- Borrow Books ----
    borrow_book("101", "M001")
    borrow_book("102", "M001")
    borrow_book("103", "M002")
    print("After borrowing some books:")
    print_state()

    # ---- Return Book ----
    return_book("101", "M001")
    print("After returning book 101 by Alice:")
    print_state()

    # ---- Search Books ----
    print("Search books by title containing 'Life':")
    results = search_books("Life")
    for book in results:
        print(book)

    print("\nSearch books by author 'Mary':")
    results = search_books("Mary", by="author")
    for book in results:
        print(book)

    # ---- Update Book & Member ----
    update_book("104", total_copies=5)
    update_member("M003", email="charlie_new@mail.com")
    print("\nAfter updates:")
    print_state()

    # ---- Delete Book & Member ----
    delete_book("105")  # should work because no copies borrowed
    delete_member("M003")  # should work because no borrowed books
    print("After deletions:")
    print_state()


if __name__ == "__main__":
    main()
