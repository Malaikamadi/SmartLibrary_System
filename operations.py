
# -------------------- Global Data Structures --------------------
BOOKS = {}  # ISBN -> {title, author, category, total_copies, original_copies}
MEMBERS = []  # List of member dicts: {member_id, name, email, borrowed_books}
CATEGORIES = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Mystery", "Romance")

# -------------------- CRUD Operations for Books --------------------

def add_book(isbn, title, author, category, total_copies):
    """
    Add a new book to BOOKS dictionary.
    Returns True if successful, False if ISBN exists or category invalid.
    """
    if isbn in BOOKS:
        return False
    if category not in CATEGORIES:
        return False
    BOOKS[isbn] = {
        "title": title,
        "author": author,
        "category": category,
        "total_copies": total_copies,
        "original_copies": total_copies
    }
    return True

def update_book(isbn, title=None, author=None, category=None, total_copies=None):
    """
    Update details of a book if exists.
    Returns True if successful, False otherwise.
    """
    if isbn not in BOOKS:
        return False
    if category is not None and category not in CATEGORIES:
        return False
    if title is not None:
        BOOKS[isbn]["title"] = title
    if author is not None:
        BOOKS[isbn]["author"] = author
    if category is not None:
        BOOKS[isbn]["category"] = category
    if total_copies is not None:
        diff = total_copies - BOOKS[isbn]["total_copies"]
        BOOKS[isbn]["total_copies"] += diff
        BOOKS[isbn]["original_copies"] += diff
    return True

def delete_book(isbn):
    """
    Delete a book if exists and no copies are borrowed.
    Returns True if successful, False otherwise.
    """
    if isbn not in BOOKS:
        return False
    if BOOKS[isbn]["total_copies"] != BOOKS[isbn]["original_copies"]:
        return False
    del BOOKS[isbn]
    return True

def search_books(query, by="title"):
    """
    Search books by title or author (case-insensitive, partial matches).
    Returns list of matching book dictionaries.
    """
    results = []
    query_lower = query.lower()
    for book in BOOKS.values():
        if by == "title" and query_lower in book["title"].lower():
            results.append(book)
        elif by == "author" and query_lower in book["author"].lower():
            results.append(book)
    return results

# -------------------- CRUD Operations for Members --------------------

def add_member(member_id, name, email):
    """
    Add a new member to MEMBERS list.
    Returns True if successful, False if member_id exists.
    """
    for m in MEMBERS:
        if m["member_id"] == member_id:
            return False
    MEMBERS.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return True

def update_member(member_id, name=None, email=None):
    """
    Update member details if exists.
    Returns True if successful, False otherwise.
    """
    for m in MEMBERS:
        if m["member_id"] == member_id:
            if name is not None:
                m["name"] = name
            if email is not None:
                m["email"] = email
            return True
    return False

def delete_member(member_id):
    """
    Delete a member if exists and has no borrowed books.
    Returns True if successful, False otherwise.
    """
    for i, m in enumerate(MEMBERS):
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) > 0:
                return False
            MEMBERS.pop(i)
            return True
    return False

# -------------------- Borrow / Return Operations --------------------

def borrow_book(isbn, member_id):
    """
    Borrow a book if available and member has less than 3 books.
    Returns True if successful, False otherwise.
    """
    if isbn not in BOOKS:
        return False
    book = BOOKS[isbn]
    if book["total_copies"] <= 0:
        return False

    for m in MEMBERS:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return False
            m["borrowed_books"].append(isbn)
            book["total_copies"] -= 1
            return True
    return False

def return_book(isbn, member_id):
    """
    Return a borrowed book.
    Returns True if successful, False otherwise.
    """
    if isbn not in BOOKS:
        return False
    for m in MEMBERS:
        if m["member_id"] == member_id:
            if isbn in m["borrowed_books"]:
                m["borrowed_books"].remove(isbn)
                BOOKS[isbn]["total_copies"] += 1
                return True
            else:
                return False
    return False
