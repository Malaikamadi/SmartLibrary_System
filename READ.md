# Mini Library Management System

## Overview
This is a console-based Mini Library Management System built in Python.  
It allows managing books, members, and borrowing/returning books using basic CRUD operations.  
The system uses **lists, dictionaries, and tuples** and does not use object-oriented programming beyond OOP-1 level.

## Features
- Add, update, delete, and search books.
- Add, update, and delete members.
- Borrow and return books (with a limit of 3 books per member).
- Track borrowed books and available copies.
- Validate genres and unique ISBN/member IDs.

## Data Structures
- **Books:** Stored in a dictionary with ISBN as the key.
- **Members:** Stored in a list of dictionaries.
- **Categories:** Stored in a tuple for validation.

## Requirements
- Python 3.12 or higher.

## How to Run
1. Make sure all files are in the same folder:
   - `operations.py`
   - `demo.py`
   - `tests.py`
2. Open terminal/command prompt in the folder.
3. To run the demo:
   ```bash
   python demo.py
