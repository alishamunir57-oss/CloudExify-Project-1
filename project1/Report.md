# Project Report — Personal Expense Tracker

**Project:** Personal Expense Tracker (CLI Application)
**Module:** Month 1, Project 1 — Python Programming Internship
**Language:** Python 3.x
**Author:** Alisha Munir


---

## 1. Overview

The Personal Expense Tracker is a command-line application built in Python that allows users to record, organize, and analyze their day-to-day expenses. The project was designed to reinforce core Python concepts — including functions, control flow, data structures, file handling, and exception handling — while producing a genuinely usable tool rather than an isolated exercise.

The application follows a menu-driven design, allowing the user to add, view, update, delete, filter, and search expenses, while automatically persisting data across sessions using file storage.

---

## 2. Objective

The primary objectives of this project were to:

- Apply Python fundamentals (loops, conditionals, functions, dictionaries, lists) in a practical, real-world context
- Implement reliable file handling for persistent data storage
- Build a robust command-line interface with proper input validation
- Practice debugging both syntax and logic-level errors through iterative testing
- Extend the base requirements with additional useful features

---

## 3. Features Implemented
- Core Functionality (as per project specification):

- Add a new expense with amount, category, and description
- View all expenses in a readable format
- View total expenses and a category-wise breakdown
- Filter expenses by category
- Save expenses to file and reload them automatically on startup
- Simple, menu-driven command-line interface

### Core Functionality (as per project specification)
- Add a new expense with amount, category, and description
- View all expenses in a readable format
- View total expenses and a category-wise breakdown
- Filter expenses by category
- Save expenses to file and reload them automatically on startup
- Simple, menu-driven command-line interface

### Additional Features (beyond specification)
- **Unique ID system** for every expense, allowing precise update and delete operations by ID rather than by name (which could be duplicated)
- **Search functionality** — expenses can be searched either by **name** or by **date**
- **Percentage breakdown** in the category summary, showing each category's share of total spending in addition to raw totals
- **Backward-compatible file loading**, supporting both earlier and current saved file formats without breaking on old data

### Input Validation
- Expense names are validated to contain only alphabetic characters
- Expense amounts must be positive numbers; zero and negative values are rejected
- Dates are validated against the `YYYY-MM-DD` format using Python's `datetime` module
- Times are validated against the `HH:MM` format using the same module
- Categories are restricted to a fixed set (Food, Transport, Shopping, Bills, Other) to prevent inconsistent or misspelled entries
- Menu input is validated to handle non-numeric entries without crashing the program

---

## 4. Technical Approach

Each expense is represented as a Python dictionary containing its ID, name, amount, date, time, and category. All expenses are held in a list during runtime, which is the primary in-memory data structure for the session.

Persistence is handled through a plain text file (`expenses.txt`), where each expense is written as a comma-separated line on exit and parsed back into dictionaries on the next startup. A global auto-incrementing counter (`next_id`) generates unique IDs for new expenses and is re-synchronized with the highest existing ID whenever data is loaded from file, ensuring IDs are never duplicated or reused — even after deletions.

All user input is wrapped in validation loops, so invalid entries (wrong date format, non-numeric amount, invalid category, etc.) prompt the user to re-enter data rather than crashing the program or silently accepting bad data.

---

## 5. Challenges Faced and Resolved

| Challenge | Resolution |
|---|---|
| Loading saved expenses caused a crash due to a mismatch between the number of fields written and the number expected when reading | Aligned the save and load formats to consistently use 5 fields, with backward compatibility for older 3-field data |
| Deleting an expense and then adding a new one could cause duplicate IDs | Replaced the `len(expenses) + 1` approach with a persistent global counter (`next_id`) that only increases, never resets |
| An indentation error caused summary output to print prematurely, before the program's welcome message | Corrected function-level indentation so all output statements execute only when the function is explicitly called |
| Name validation logic was briefly inverted during a refactor, rejecting valid names | Identified through manual testing and corrected the boolean condition |

Each of these was identified through **manual testing of edge cases** (e.g., deleting then re-adding expenses, submitting invalid categories, restarting the program to test file reload) rather than relying solely on the program appearing to work during a single run.

---

## 6. Key Learnings

- How to structure a multi-feature CLI application using functions for modularity and readability
- Practical file handling for persistent storage, including safely parsing external data that may be malformed or incomplete
- The importance of testing beyond the "happy path" — many of the bugs found in this project only appeared under specific sequences of actions (e.g., delete-then-add), not during normal single-pass testing
- The difference between a syntax error and a logic error, and how the latter is often harder to detect since the program runs without crashing but produces incorrect behavior
- Writing defensive code that validates user input at every entry point rather than assuming well-formed input

---

## 7. Conclusion

The Personal Expense Tracker successfully implements all features outlined in the project specification and extends beyond it with ID-based operations, dual-mode search, and percentage-based analytics. Through iterative testing and debugging, the application was refined to handle edge cases gracefully rather than only working under ideal conditions. This project strengthened both my practical Python skills and my understanding of how to systematically test and debug a growing codebase.

---

## 8. How to Run

```bash
python expenses.py
```
