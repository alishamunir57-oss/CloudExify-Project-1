students=[]
next_id=1

#----------- Generates a unique ID for each student--------------

def generate_id():
    global next_id
    current_id=next_id
    next_id+=1      
    return current_id
#---------------Display student------------------

def display_student(student):

    print("-----------------------------------")
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Father Name:", student["father_name"])
    print("Phone:", student["phone"])
    print("Email:", student["email"])
    print("Class:", student["class"])
    print("Attendance:", student["attendance"], "%")

# --------Adds a new student with subjects and grades--------

def addstudent():
    student = {}
    while True:
        name = input("Enter student name: ")
        if name.strip() and all(c.isalpha() or c in " -" for c in name):
         name=name.title()
         break
        else:
            print("Invalid name.Please enter valid name")
        
    for s in students:
        if s["name"].lower()==name.lower():
            print(f"Student '{name}'already exist!")
            return
    father_name=input("Enter fathers's name").title()

    while True:
        phone= input("Enter contact number")
        if phone.isdigit() and len(phone)==11 and phone.startswith("03"):
            break
        else:
            print("Enter valid 11 digit number")

    while True:
        email= input("Enter email:")

        if( email.count("@")==1 and "." in email.split("@")[1] ):
            break
        else:
            print("Invalid email")

    while True:
       student_class= input("Enter class of student")
       if student_class:
           break
       print(" Class cannot be empty ")

    grades={}
    while True:

       num_subjects = input("Enter number of subjects: ")
       if num_subjects.isdigit() and 0 < int(num_subjects)<100:
         num_subjects=int(num_subjects)
         break
       else:
            print("Please enter a valid number")


    for i in range(num_subjects):

      while True:
        while True:
            subject = input(f"Enter subject name of {i+1}: ").strip().title()

            if subject.replace(" ", "").replace("-", "").isalpha():
              break
            else:
             print("Invalid subject name")

        subject = subject.strip().title()

        if subject in grades:
          print("Subject already exist")
          continue
        else:
            break

      while True:
         grade = input(f"Enter grade for {subject}: ")

         if grade.isdigit() and 0 <= int(grade) <= 100:
            grades[subject] = int(grade)
            break
         else:
            print("Invalid grade")


    student={
        "id": generate_id(),
        "name": name,
        "father_name":father_name,
        "phone":phone,
        "email":email,
        "class":student_class,
        "grades": grades,
        "attendance": 0
    }
    students.append(student)
    print("Student added successfully")



def calculate_average(student):
    grades = student["grades"].values()
    if len(grades)==0:
        return 0 
    return sum(grades) / len(grades)

# -----------Displays all students with their grades and average------

def viewstudent():
    if len(students)==0:
        print("No students in the list.")
        return
    print("==========Student List=========")
    for student in students:
            display_student(student)
            print("Subjects and Grades")
            for subjects, grade in student["grades"].items():
                print(f"{subjects}:{grade}")

            print(f"Average: {calculate_average(student):.2f}%")


# --------- Removes a student from the system ---------

def remove_student():

    if len(students) == 0:
        print("No students to remove.")
        return

    print("Remove student by:")
    print("1. Name")
    print("2. ID")

    choice = input("Enter your choice: ")

    # ---------- Remove by Name ----------
    if choice == "1":

        name = input("Enter student name: ").strip().title()

        for student in students:

            if student["name"] == name:

                confirm = input(f"Remove {student['name']} (ID: {student['id']})? (y/n): ")

                if confirm.lower() in ("y", "yes"):

                    students.remove(student)
                    print("Student removed successfully.")

                else:
                    print("Operation cancelled.")

                return

        print("Student not found.")

    # ---------- Remove by ID ----------
    elif choice == "2":

        sid = input("Enter student ID: ")

        if not sid.isdigit():
            print("Invalid ID.")
            return

        sid = int(sid)

        for student in students:

            if student["id"] == sid:

                confirm = input(f"Remove {student['name']} (ID: {student['id']})? (y/n): ")

                if confirm.lower() in ("y", "yes"):

                    students.remove(student)
                    print("Student removed successfully.")

                else:
                    print("Operation cancelled.")

                return

        print("Student not found.")

    else:
        print("Invalid choice.")

# ---------Searches a student by name or ID--------
    
def search_student():
    if len(students)==0:
        print("No students to search.")
        return
    
    print("search by:")
    print("1. Name")
    print("2. Id")

    search_choice=input("Enter your choice:")

    found=False

    if search_choice=="1":
       name=input("Enter Student name ")

       for student in students:
        if name.lower() in student["name"].lower():
                
                display_student(student)
                print("Subjects and Grades: ")
                for subject,grade in student["grades"].items():
                    print(f"{subject}:{grade}")
                found = True
                break
    elif search_choice=="2":
        search_id=input("Enter student ID: ")

        if not search_id.isdigit():
            print("Invalid ID format")
            return
        
        search_id= int(search_id)

        for student in students:
            if student["id"] == search_id:
                print("\nStudent Found")
                display_student(student)
                print("Subjects and Grades: ")
                for subject,grade in student["grades"].items():
                    print(f"{subject}:{grade}")
    
                found = True
                break   
    if not found:
        print("Student not found. ")
  
# ------------Updates the grade of a student's selected subject------------

def edit_grade():

    if len(students)==0:
        print("No students to edit grades for.")
        return
    
    print("Available students:")

    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']}")

    print("Edit by:")
    print("1.name")
    print("2. ID")

    choice=input("Enter your choice")
    
    if choice=="1":
        value=input("Enter student name:").lower()
        for student in students:
            if student["name"].lower()== value:
                subject=input("Enter subject to edit").strip().title()

                if subject in student["grades"]:
                    new_grade=input("Enter new grade")
                    if new_grade.isdigit() and 0<=int(new_grade)<=100:
                        student["grades"][subject] = int(new_grade)
                        print("Grade updated successfully")
                    else: print("Invalid Grade. ")
                else:
                    print("Subject not found")

                return
    elif choice=="2":
        value=input("Enter student ID: ")
        if not value.isdigit():
                print("Invalid ID")
                return
        value= int(value)

        for student in students:
            if student["id"]== value:
                subject= input("Enter subject to edit ").strip().title()

                if subject in student["grades"]:
                    new_grade=input("Enter new grade: ")
                    if new_grade.isdigit() and 0<= int(new_grade)<=100:
                      student["grades"][subject]= int(new_grade)
                      print("Grade added successfully")
                    else:
                        print("Invalid Grade")
                else:
                    print("Subject not found ")

                return
    print("Student not found")


## -------- Update Attendance --------

def update_attendance():

    if len(students)==0:
        print("No students available.")
        return


    sid=input("Enter student ID: ")

    if not sid.isdigit():
        print("Invalid ID")
        return

    sid=int(sid)


    for student in students:

        if student["id"] == sid:

            attendance=input("Enter attendance percentage: ")

            if attendance.isdigit() and 0 <= int(attendance)<=100:

                student["attendance"]=int(attendance)

                print("Attendance updated successfully")

            else:
                print("Invalid attendance")

            return


    print("Student not found")


# ------------Calculates the average marks of a student---------

def calculate_grade(avg):

    

    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"
    
    elif avg>=50:
        return "D"

    else:
        return "F"



# --------- Generates performance remarks ---------

def calculate_remarks(avg):

    if avg >= 90:
        return "Excellent Performance"

    elif avg >= 80:
        return "Very Good Performance"

    elif avg >= 70:
        return "Good Performance"

    elif avg >= 60:
        return "Satisfactory"

    elif avg >= 50:
        return "Needs Improvement"

    else:
        return "Poor Performance"

#-------------------Calculates the position of the student-------------

def calculate_position(student):

    ranking = []

    for s in students:
        avg = calculate_average(s)
        ranking.append((s["id"], avg))

    ranking.sort(key=lambda x: x[1], reverse=True)

    for position, (sid, avg) in enumerate(ranking, start=1):

        if sid == student["id"]:
            return position
        
    

# --------Generates a complete report card for a student---------

def class_report():

    if len(students) == 0:
        print("No students in the class.")
        return

    ranking = []

    pass_count = 0
    fail_count = 0
    total_average = 0

    for student in students:

        avg = calculate_average(student)

        ranking.append((student["name"], avg))

        total_average += avg

        if avg >= 50:
            pass_count += 1
        else:
            fail_count += 1

    ranking.sort(key=lambda x: x[1], reverse=True)

    class_average = total_average / len(students)

    highest = ranking[0]
    lowest = ranking[-1]

    print("\n========== CLASS REPORT ==========")
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest Average: {highest[0]} ({highest[1]:.2f})")
    print(f"Lowest Average: {lowest[0]} ({lowest[1]:.2f})")
    print(f"Total Student: {len(students)}")
    print(f"Passed Students: {pass_count}")
    print(f"Failed Students: {fail_count}")

    print("\n========== RANKING ==========")

    for rank, (name, avg) in enumerate(ranking, start=1):
        remarks= calculate_remarks(avg)
        print(f"{rank}. {name} - {avg:.2f}% -{remarks}")


#------------Printing subject wise class Average-----------------

def subject_wise_average():

    if len(students) == 0:
        print("No students available.")
        return

    subjects = {}

    for student in students:
        for subject, grade in student["grades"].items():

            if subject not in subjects:
                subjects[subject] = []

            subjects[subject].append(grade)


    print("\n======= SUBJECT WISE CLASS AVERAGE =======")

    for subject, marks in subjects.items():

        average = sum(marks) / len(marks)

        print(f"{subject}: {average:.2f}")
    

#---------Printing Report Card of each student-----------

def print_report_card(student):
    avg = calculate_average(student)
    grade = calculate_grade(avg)
    percentage = avg   # marks are out of 100, so average == percentage
    position= calculate_position(student)
    remarks= calculate_remarks(avg)

    print("=" * 50)
    print("STUDENT REPORT CARD".center(50))
    print("=" * 50)
    print(f"{'ID':<10} : {student['id']}")
    print(f"{'Name':<10} : {student['name']}")
    print(f"{'Percentage':<10} : {percentage:.2f}%")
    print(f"{'Average':<10} : {avg:.2f}")
    print(f"{'Grade':<10} : {grade}")
    print(f"{'Position': <10}: {position}")
    print(f"{'Remarks':<10}: {remarks}")
    print(f"{'Attendance':<10} : {student.get('attendance',0)}%")
    print(f"{'Total Subjects':<10}: {len(student['grades'])}")
    print("-" * 50)
    print(f"{'Subject':<30}{'Marks'}")
    print("-" * 50)
    for subject, marks in student["grades"].items():
        print(f"{subject:<30}{marks:>5}")
    print("-" * 50)


# ---------Generates class summary, statistics, and ranking----------

def report_card():
    if len(students) == 0:
        print("No students available.")
        return

    print("Print report card by:")
    print("1. Name")
    print("2. ID")

    choice = input("Enter your choice: ")
    found = False

    if choice == "1":
        name = input("Enter student name: ")
        for student in students:
            if student["name"].lower() == name.lower():
                print_report_card(student)
                found = True
                break

    elif choice == "2":
        sid = input("Enter student ID: ")
        if not sid.isdigit():
            print("Invalid ID.")
            return
        sid = int(sid)
        for student in students:
            if student["id"] == sid:
                print_report_card(student)
                found = True
                break

    else:
        print("Invalid choice.")
        return

    if not found:
        print("Student not found.")



# -------- Export Report --------

def export_report():

    if len(students)==0:
        print("No students available.")
        return


    sid=input("Enter student ID: ")

    if not sid.isdigit():
        print("Invalid ID")
        return


    sid=int(sid)


    for student in students:

        if student["id"]==sid:

            filename = student["name"]+"_report.txt"


            with open(filename,"w") as file:


                avg=calculate_average(student)
                grade=calculate_grade(avg)
                position=calculate_position(student)
                remarks=calculate_remarks(avg)


                file.write("==============================\n")
                file.write("       STUDENT REPORT CARD\n")
                file.write("==============================\n\n")


                file.write(f"ID: {student['id']}\n")
                file.write(f"Name: {student['name']}\n")
                file.write(f"Average: {avg:.2f}\n")
                file.write(f"Percentage: {avg:.2f}%\n")
                file.write(f"Grade: {grade}\n")
                file.write(f"Position: {position}\n")
                file.write(f"Remarks:  {remarks}\n")


                file.write(f"Attendance: {student.get('attendance',0)}%\n\n")


                file.write("------------------------------\n")
                file.write(f"{'Subject':<20}{'Marks'}\n")
                file.write("------------------------------\n")


                for subject,marks in student["grades"].items():

                    file.write(f"{subject:<15}{marks}\n")


            print("Report exported successfully!")

            return


    print("Student not found")




#----------------- Saves student records into a CSV file---------------
import csv

def save_to_csv():

    if len(students) == 0:
        print("No students to save.")
        return

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Father Name", "Phone", "Email", "Class", "Attendance", "Subject", "Grade"])

        for student in students:
            for subject, grade in student["grades"].items():

                writer.writerow([
                    student["id"],
                    student["name"],
                    student.get("father_name", ""),
                    student.get("phone", ""),
                    student.get("email", ""),
                    student.get("class", ""),
                    student.get("attendance", 0),
                    subject,
                    grade
                ])

    print("Data saved successfully to students.csv")

# ------------Loads student records from a CSV file------------


import csv

def load_from_csv():
    global students
    global next_id

    try:
        students.clear()

        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:

                student_id = int(row["ID"])
                name = row["Name"]
                father_name=row["Father Name"]
                phone = row["Phone"]
                email = row["Email"]
                student_class = row["Class"]
                attendance = int(row["Attendance"])
                subject = row["Subject"]
                grade = int(row["Grade"])

                found = False

                for student in students:
                    if student["id"] == student_id:

                        student["grades"][subject] = grade
                        found = True
                        break


                if not found:
                    students.append({
                        "id": student_id,
                        "name": name,
                        "father_name": father_name,
                        "phone": phone,
                        "email": email,
                        "class": student_class,
                        "attendance": attendance,
                        "grades": {
                            subject: grade
                        }
                    })

        if len(students) > 0:
            next_id = max(student["id"] for student in students) + 1

        print("Data loaded successfully!")

    except FileNotFoundError:
        print("students.csv not found.")


# -----------Displays the main menu and controls program flow----------

def main():
    print("Welcome to the Student Management System")
    while True:
        print("\n==========Menu=====================")

        print("1. Add Student")
        print("2. View Students")   
        print("3. Search Student")
        print("4. Edit Grade")
        print("5. Class Report")
        print("6. Report Card")
        print("7. Save to CSV ")
        print("8. Load from CSV ")
        print("9. Remove Student")
        print("10. Subject Wise Average")
        print("11. Update Attendance")
        print("12. Export Report")
        print("13. Exit")  
        choice=input("Enter your choice (1-13): ")
        if choice=='1':
            addstudent()
        elif choice=='2':
            viewstudent()
        elif choice=='3':
            search_student()
        elif choice=='4':
            edit_grade()
        elif choice=='5':
            class_report()
        elif choice=='6':
            report_card()
        elif choice=='7':
            save_to_csv()
        elif choice=='8':
            load_from_csv()
        elif choice=='9':
            remove_student()
        elif choice=='10':
            subject_wise_average()
        elif choice=='11':
            update_attendance()
        elif choice=='12':
             export_report()
        elif choice=='13':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()