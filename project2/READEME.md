# Student Grade Management System

**CloudExify Python Internship 2026 — Month 1, Project 2**

- **Name:** [Alisha Munir]
- **Type:** Command Line Interface (CLI) Application
- **Language:** Python 3.x

---

## 1. Project Overview

A command-line Student Grade Management System that lets a user add students with full profile details, record grades across custom subjects, view records, generate class reports with rankings and remarks, edit grades, track attendance, remove students with confirmation, and save/load data using CSV files.

---

## 2. Core Features

| Feature | Description |
|---|---|
| Add Student | Add name, father's name, phone, email, class, and any number of subjects/grades |
| View All Students | Display every student's full profile, subjects, grades, and average |
| Search Student | Search by name (partial match) or exact ID |
| Edit Grade | Update a subject's grade by student name or ID |
| Remove Student | Delete a student by name or ID, with a confirmation prompt |
| Class Report | Class-wide average, highest, lowest, pass/fail count, ranking with remarks |
| Save to CSV | Save all student data to `students.csv` |
| Load from CSV | Restore previously saved data |

## 3. Bonus Features Implemented

| Bonus | Description |
|---|---|
| Extended Student Profile | Father's name, validated phone, validated email, non-empty class field |
| Custom Subjects | Any subject name allowed per student; duplicates rejected and re-prompted |
| Letter Grades | Six-tier scale (A+, A, B, C, D, F) |
| Performance Remarks | Descriptive remark per average (e.g. "Excellent Performance", "Needs Improvement") |
| Class Position/Rank | Each student's rank within the class shown on their individual report card |
| Individual Report Card | Formatted report card with grade, position, remarks, attendance, and subject count |
| Attendance Tracking | Validated 0–100% attendance per student |
| Subject-Wise Class Average | Average per individual subject across the whole class |
| Export Report to Text File | Writes a student's full report card to a `.txt` file |
| Delete Confirmation | Removal by name or ID requires explicit "y" confirmation |
| Reusable Display Helper | `display_student()` centralizes profile printing, used across View, Search, and Remove |

---

## 4. Data Structure

```python
student = {
    "id": 1,
    "name": "Alisha",
    "father_name": "Ahmed Khan",
    "phone": "03001234567",
    "email": "alisha@example.com",
    "class": "10th",
    "grades": {
        "Math": 90,
        "English": 87
    },
    "attendance": 85
}
```

---

## 5. Functions

| Function | Purpose |
|---|---|
| `generate_id()` | Unique auto-incrementing student ID |
| `display_student(student)` | Prints a student's core profile fields — reused across multiple features |
| `addstudent()` | Adds a student with full profile, validated subjects/grades, duplicate checks |
| `calculate_average(student)` | Average of a student's grades (0 if empty) |
| `viewstudent()` | Lists all students with profile, subjects, grades, and average |
| `remove_student()` | Removes a student by name or ID, with confirmation |
| `search_student()` | Searches by partial name match or exact ID |
| `edit_grade()` | Updates a subject's grade by student name or ID |
| `update_attendance()` | Sets a validated attendance percentage |
| `calculate_grade(avg)` | Converts average to letter grade (A+ to F) |
| `calculate_remarks(avg)` | Converts average to a descriptive performance remark |
| `calculate_position(student)` | Calculates a student's rank within the class |
| `class_report()` | Class average, highest/lowest, pass/fail counts, ranking with remarks |
| `subject_wise_average()` | Average per subject across the whole class |
| `print_report_card()` / `report_card()` | Formatted individual report card with position and remarks |
| `export_report()` | Writes a student's full report card to a `.txt` file |
| `save_to_csv()` / `load_from_csv()` | CSV persistence for all student data |
| `main()` | Menu loop and routing |

---

## 6. Design Decisions

- **Custom subjects instead of a fixed list** — more realistic, since students can have different electives. Trade-off: CSV storage uses one row per subject rather than one row per student.
- **`display_student()` helper** — introduced to avoid repeating the same profile-printing code across View, Search, and Remove; a small step toward DRY (Don't Repeat Yourself) code organization.
- **Dictionaries and lists over classes/OOP** — this project intentionally follows the guide's Month 1 curriculum (nested dictionaries, list of dictionaries), which does not introduce classes. A class-based (`Student` object) redesign was considered but deliberately left for a possible future refactor, since OOP is typically a later-stage concept and switching now would risk destabilizing a working, tested project close to submission.
- **No login/logout system** — considered, but intentionally left out. This is a single-user offline tool, so authentication doesn't protect anything real here, and implementing it without proper password hashing would introduce more risk than value.

---

## 7. Sample Output

```
==================================================
             STUDENT REPORT CARD
==================================================
ID         : 1
Name       : Alisha
Percentage : 88.50%
Average    : 88.50
Grade      : A
Position   : 1
Remarks    : Very Good Performance
Attendance : 85%
Total Subjects: 2
--------------------------------------------------
Subject                       Marks
--------------------------------------------------
Math                              90
English                           87
--------------------------------------------------
```

---

## 8. Testing

| # | Test Case | Steps | Expected Result | Actual Result | Status |
|---|-----------|-------|------------------|----------------|--------|
| 1 | Add student with valid full profile | Add student with valid name, father's name, phone, email, class, subjects, grades | Student saved with all fields | Added successfully | ✅ Pass |
| 2 | Add student with invalid phone | Enter a number not 11 digits or not starting with "03" | Rejected, re-prompted | Showed error, re-asked | ✅ Pass |
| 3 | Add student with invalid email | Enter text with no "@" or no domain period | Rejected, re-prompted | Showed "Invalid email", re-asked | ✅ Pass |
| 4 | Add student with empty class field | Press Enter with no input for class | Rejected, re-prompted | Showed "Class cannot be empty", re-asked | ✅ Pass |
| 5 | Add duplicate student name | Add the same name twice | Error message, not added | Showed "already exist!" | ✅ Pass |
| 6 | Add duplicate subject for same student | Enter the same subject twice while adding one student | Rejected, re-prompted at the same slot | Correctly re-asked | ✅ Pass |
| 7 | Add grade greater than 100 | Enter 199 for a grade | Rejected, re-prompted | Showed "Invalid grade", re-asked | ✅ Pass |
| 8 | View list with multiple students | Add 5+ students, then view all | Full profile, subjects, grades, average shown | Displayed correctly | ✅ Pass |
| 9 | Search by partial name | Search a substring of an existing name | Full profile displayed | Found and displayed correctly | ✅ Pass |
| 10 | Search non-existing student | Search a name not in the list | "Not found" message | Displayed correctly | ✅ Pass |
| 11 | Search student by ID | Search by exact numeric ID | Correct student displayed | Displayed correctly | ✅ Pass |
| 12 | Edit grade by student name (valid) | Update an existing subject's grade using name-based lookup | Grade updates correctly | Updated successfully | ✅ Pass |
| 13 | Edit grade by student ID (valid) | Update an existing subject's grade using ID-based lookup | Grade updates correctly | Updated successfully | ✅ Pass |
| 14 | Edit grade by name — invalid input | Enter non-numeric text (e.g. "abc") as the new grade | Rejected with a clear error message, no crash | Showed "Invalid Grade." — no crash | ✅ Pass |
| 15 | Edit grade by ID — invalid input | Enter non-numeric text as the new grade via ID-based lookup | Rejected with a clear error message, no crash | No crash occurs, but no error message shown either (silent fail) — see Known Issues | ⚠️ Minor gap |
| 16 | Edit grade — out-of-range value | Enter 150 as the new grade | Rejected, not saved | Rejected correctly in both branches | ✅ Pass |
| 17 | Edit grade — subject not found | Enter a subject the student doesn't have | "Subject not found" message | Shown correctly in both branches | ✅ Pass |
| 18 | Edit grade — student not found | Enter a name/ID that doesn't exist | "Student not found" message | Shown correctly | ✅ Pass |
| 19 | Remove student by name, not first in list | Remove a student that isn't first in the list | Correct student found and removed after confirmation | Removed correctly | ✅ Pass |
| 20 | Remove student by ID | Remove using the ID-based option | Correct student found and removed after confirmation | Removed correctly | ✅ Pass |
| 21 | Remove — cancel confirmation | Choose "n" when asked to confirm | Student is not removed | Showed "Operation cancelled." | ✅ Pass |
| 22 | Update attendance — valid and invalid | Set 85 (valid) and 150 (invalid) | Valid accepted, invalid rejected | Both handled correctly | ✅ Pass |
| 23 | Class report with ranking and remarks | Run with 5+ students | Correct stats, ranking, and remarks per student | All correct | ✅ Pass |
| 24 | Individual report card with position | View a report card for a specific student | Correct rank and remark shown alongside grade | Displayed correctly | ✅ Pass |
| 25 | Subject-wise class average | Run with students sharing subjects | Correct average per subject | Correct | ✅ Pass |
| 26 | Export report to text file | Export a valid student's report | `.txt` file created matching on-screen report | File created correctly | ✅ Pass |
| 27 | Save to CSV, Load from CSV, View | Full round-trip test | All fields preserved exactly | Confirmed correct | ✅ Pass |

---


## 9. Bugs Found During Development & Resolutions

| Bug | Description | Resolution |
|---|---|---|
| Grade collection outside loop | Only the last subject's grade was ever recorded due to incorrect indentation | Re-indented the block inside the `for` loop |
| String/int comparison errors | `.isdigit()` called on already-converted integers, causing crashes | Validate the raw string first, convert only after |
| Assignment vs comparison typo | `==` used instead of `=` when updating a grade | Corrected the operator |
| Case-sensitive subject matching | Same subject typed with different casing treated as different keys | Normalized with `.strip().title()` at entry time |
| CSV save/load data loss | Profile fields and attendance weren't saved or restored | Extended both functions to include every field |
| Attendance default type mismatch | Defaulted to `{}` instead of `0` | Changed default to `0` |
| Duplicate-subject loop skip | `continue` skipped to the next subject slot instead of re-prompting the same one | Wrapped in a nested `while True` |
| Early return in `remove_student()` | Function exited after checking only the first student | Moved `return` inside the `if` block |
| Email validation typo | Checked for a comma instead of a period in the domain | Corrected to check for `"."` |
| Edit Grade — name branch crash | `int(input(...))` converted before validation, then `.isdigit()` was called on an integer, causing a crash | Kept input as a string, validated with `.isdigit()` and range check first, converted only after |

---


## 10. How to Run

```bash
python grade_system.py
```

Data is saved to and loaded from `students.csv`. Individual report cards export as `<StudentName>_report.txt`.
