# tests.py
from operations import add_book, add_member, update_book, update_member
from operations import delete_book, delete_member, borrow_book, return_book
from operations import BOOKS, MEMBERS

# ---- Book Tests ----
assert add_book("201", "Test Book", "Author A", "Fiction", 2) == True
assert add_book("201", "Duplicate ISBN", "Author B", "Fiction", 1) == False  # duplicate ISBN
assert update_book("201", title="Updated Book") == True
assert delete_book("201") == True  # can delete because not borrowed

# ---- Member Tests ----
assert add_member("T001", "Test Member", "test@mail.com") == True
assert add_member("T001", "Duplicate Member", "test2@mail.com") == False  # duplicate ID
assert update_member("T001", email="new@mail.com") == True
assert delete_member("T001") == True  # can delete because no borrowed books

# ---- Borrow / Return Tests ----
add_book("301", "Borrow Book", "Author C", "Mystery", 1)
add_member("M100", "Borrower", "borrow@mail.com")
assert borrow_book("301", "M100") == True
assert borrow_book("301", "M100") == False  # no copies left
assert return_book("301", "M100") == True
assert return_book("301", "M100") == False  # already returned
assert borrow_book("999", "M100") == False  # book does not exist
assert borrow_book("301", "M999") == False  # member does not exist

print("All tests passed successfully!")
