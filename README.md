# Mini Library Management System

 Course: Object-Oriented Programming 1 (OOP1)
 Student: Alimatu Maliaka Jalloh


## Overview
This project is a Mini Library Management System implemented in Python.  
It demonstrates the use of lists, dictionaries, tuples, and functions to perform CRUD (Create, Read, Update, Delete) operations.  
The system simulates real-world library tasks such as managing books, registering members, and handling borrowing and returning of books in a simple console-based environment.


## Features
- Add, update, search, and delete books.
- Add, update, and delete library members.
- Borrow and return books with loan limits (maximum of 3 books per member).
- Data validation for unique ISBNs and valid categories.
- All data stored in memory (no database required).


## Data Structures Used
- **Dictionary:** Used to store books with ISBN as the key and book details as values.
- **List:** Used to store member records as dictionaries.
- **Tuple:** Used to store predefined valid book categories.



## File Descriptions
| File Name | Description |
|------------|-------------|
| `operations.py` | Contains all CRUD operations and borrow/return logic. |
| `demo.py` | Demonstrates how the system works using sample data and prints outputs. |
| `tests.py` | Includes assert-based unit tests for key system functionalities. |
| `README.md` | Project documentation and setup instructions. |
| `UML.png` | Hand-drawn UML diagram showing data relationships and function interactions. |
| `DesignRationale.pdf` | Explains design choices, structure, and data integrity. |

---

## How to Run the Project

### 1. Open the project in PyCharm or any Python IDE.
### 2. Ensure you are in the project’s main directory (where all `.py` files are located).
### 3. Run the demo script:
```bash
python demo.py



