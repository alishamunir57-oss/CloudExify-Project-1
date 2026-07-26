import datetime
expenses=[]
next_id = 1
def get_next_id():
    global next_id
    current = next_id
    next_id += 1
    return current
def add_expense():
        while True:
             
         expense_name = input("Enter expense name: ")
         
         if expense_name.replace(" ", "").replace(" ", " ").isalpha()==False:
          print("Invalid input. Please enter a valid name for expense.")
          continue
         while True:
             try:
                 expense_amount = float(input("Enter expense amount: "))
                 if expense_amount <= 0:
                     print("Expense amount cannot be zero or negative.")
                     continue
                 break
             except ValueError:
                 print("Invalid input. Please enter a valid number for expense amount.")
         expense_date = input("Enter expense date (YYYY-MM-DD): ")
         while True:
          try:
            datetime.datetime.strptime(expense_date, '%Y-%m-%d')
            break
          except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")
            expense_date = input("Enter expense date (YYYY-MM-DD): ")   
         while True:
          expense_time = input("Enter expense time (HH:MM): ")
          try:
            datetime.datetime.strptime(expense_time, '%H:%M')
            break
          except ValueError:
            print("Invalid time format. Please enter in HH:MM format.")
         if expense_amount <= 0:
          print("Expense amount cannot be zero or negative.")
          return
         print("Select expense category:")
         while True:
           expense_category=input("Food, Transport, Shopping, Bills, Other: ")
           if expense_category.lower() == "food" or expense_category.lower() == "transport" or expense_category.lower() == "shopping" or expense_category.lower() == "bills" or expense_category.lower() == "other":
             break
           else:
            print("Invalid category. Please select from the given options.")
            print("Categories are: Food, Transport, Shopping, Bills, Other")
         expenses.append({"id": get_next_id(), "name":expense_name,"amount":expense_amount,"date":expense_date,"time":expense_time,"category":expense_category})
         print("Expense added successfully.")
         answer = input("Do you want to add more expenses? (yes/no): ")
         if answer.lower() == "yes":
          continue
         elif answer.lower() == "no":
          return
         else:
             print("Invalid input. Please enter 'yes' or 'no'.")
 
def view_expenses():
    if len(expenses)==0:
        print("No expenses to view.")
        return

    for expense in expenses:
     
     print(f"ID       : {expense['id']}")
     print(f"Name     : {expense['name']}")
     print(f"Amount   : {expense['amount']}")
     print(f"Date     : {expense['date']}")
     print(f"Time     : {expense['time']}")
     print(f"Category : {expense['category']}")
     print("------------------------------------------")
     print("------------------------------------------")
    print(f"Total Expenses Recorded: {len(expenses)}")
def delete_expense():
    if len(expenses)==0:
        print("No expenses to delete.")
        return
    
    for expense in expenses:
     print(f"ID       : {expense['id']}")
     print(f"Name     : {expense['name']}")
     print(f"Amount   : {expense['amount']}")
     print(f"Date     : {expense['date']}")
     print(f"Time     : {expense['time']}")
     print(f"Category : {expense['category']}")
     print("------------------------------------------")
    delete_id=input("Enter the ID of the expense you want to delete:")
    found=False     
    for expense in expenses:
        if expense["id"] == int(delete_id):
            expenses.remove(expense)
            found=True
            print("Expense deleted successfully.")
            break
    if found==False:
        print("Expense not found.")   
def update_expense():
        if len(expenses)==0:
            print("No expenses to update.")
            return
        while True:
            try:
                update_id=int(input("Enter the ID of the expense you want to update:"))
                break
            except ValueError:
                print("Invalid ID. Please enter a valid ID.")
        found=False
        for expense in expenses:
            if expense["id"] == int(update_id):
                found=True
                print("Updating expenses...")
                while True: 
                    try:
                        expense["amount"]=int(input("Enter new amount: "))
                        if expense["amount"] <= 0:
                            print("Expense amount cannot be zero or negative.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for expense amount.")
                while True:

                 expense["category"]=input("Enter new category: ")
                 if expense["category"].lower() in ["food", "transport", "shopping", "bills", "other"]:
                     break
                 print("Invalid category. Please select from the given options.")
                 print("Categories are: Food, Transport, Shopping, Bills, Other")
                for expense in expenses:
                    if expense["category"].lower() not in ["food", "transport", "shopping", "bills", "other"]:
                        print("Invalid category. Please select from the given options.")
                        print("Categories are: Food, Transport, Shopping, Bills, Other")
                        continue
                expense["name"]=input("Enter new name: ")
                if expense["name"].replace(" ", "").replace(" ", " ").isalpha()==False: 
                    print("Invalid input. Please enter a valid name for expense.")
                    continue
                
                while True:
                    expense["date"]=input("Enter new date (YYYY-MM-DD): ")
                    try:
                        datetime.datetime.strptime(expense["date"], '%Y-%m-%d')
                        break
                    except ValueError:
                        print("Invalid date format. Please enter in YYYY-MM-DD format.")
                while True:
                    expense["time"]=input("Enter new time (HH:MM): ")
                    try:
                        datetime.datetime.strptime(expense["time"], '%H:%M')
                        break
                    except ValueError:
                        print("Invalid time format. Please enter in HH:MM format.")
                print("Expense updated successfully.")
        if not found:
                print("Expense not found.")
    
def filter_expenses():
        print("Filtering by category...")
        filter_category=input("Enter category to filter by:")
        found=False
        for expense in expenses:
            if expense["category"].lower() == filter_category.lower():
                print("ID",expense["id"],"Name",expense["name"],"Amount",expense["amount"],"Date",expense["date"],"Time",expense["time"],"Category",expense["category"])
                found=True
        if not found:
                print("No expenses found in this category.")
def category_summary():
        print("Category Summary:")
        food, transport, shopping, bills, other = 0, 0, 0, 0, 0
        total_expense=0
        for expense in expenses:
            if expense["category"].lower()=="food":
                food+=expense["amount"]
            elif expense["category"].lower()=="transport":
                transport+=expense["amount"]
            elif expense["category"].lower()=="shopping":
                shopping+=expense["amount"]
            elif expense["category"].lower()=="bills":
                bills+=expense["amount"]
            else:
                other+=expense["amount"]
            total_expense+=expense["amount"]
        #Percentage calculation
        food_percentage = (food / total_expense) * 100 if total_expense > 0 else 0
        transport_percentage = (transport / total_expense) * 100 if total_expense > 0 else 0
        shopping_percentage = (shopping / total_expense) * 100 if total_expense >   0 else 0
        bills_percentage = (bills / total_expense) * 100 if total_expense > 0 else 0
        other_percentage = (other / total_expense) * 100 if total_expense > 0 else 0
        print(f"Food: {food} ({food_percentage:.2f}%)")  
        print(f"Transport: {transport} ({transport_percentage:.2f}%)")
        print(f"Shopping: {shopping} ({shopping_percentage:.2f}%)")
        print(f"Bills: {bills} ({bills_percentage:.2f}%)")
        print(f"Other: {other} ({other_percentage:.2f}%)")
        print("Total Expense:", total_expense)
def save_and_exit():
        print("Saving and exiting...")
        with open("expenses.txt","w") as f:
            for expense in expenses:
                f.write(f"{expense['name']},{expense['amount']},{expense['date']},{expense['time']},{expense['category']}\n")
        print("Expenses saved successfully.")
        exit()
def load_expenses():
    try:
        with open("expenses.txt", "r") as f:
            id = 1

            for line in f:
                line = line.strip()

                if not line:
                    continue

                data = line.split(",")

                if len(data) == 5:
                    name, amount, date, time, category = data

                elif len(data) == 3:
                    name, amount, category = data
                    date = "N/A"
                    time = "N/A"

                expenses.append({
                    "id": id,
                    "name": name,
                    "amount": float(amount),
                    "date": date,
                    "time": time,
                    "category": category
                })

                id += 1
            global next_id
            next_id = id

        print("Previous expenses loaded successfully.")

    except FileNotFoundError:
        print("No previous expenses found.")
def search():
    print("Search by:")
    print("1. Name")
    print("2. Date")
    search_choice = input("Enter your choice (1 or 2): ")
    found=False  
    if search_choice == "1":
        search_name = input("Enter the name of the expense to search: ")  
        for expense in expenses:
         if expense["name"].lower() == search_name.lower():
            print("ID:", expense["id"])
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Date:", expense["date"])
            print("Time:", expense["time"])
            print("Category:", expense["category"])
    if search_choice == "2":
        search_date = input("Enter the date of the expense to search (YYYY-MM-DD): ")  
        for expense in expenses:
         if expense["date"] == search_date:
            print("ID:", expense["id"])
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Date:", expense["date"])
            print("Time:", expense["time"])
            print("Category:", expense["category"])
            found=True

load_expenses()
while True:
     print("\nWelcome to the Expense Tracker!")
     print("==================================== EXPENSE TRACKER====================================")
     print("1.Add expense\n2.View expenses\n3.Delete expense\n4.Update expense\n5.Filter by category\n6.Category summary\n7.Save and exit\n8.Search expense")
     try:
       choice=int(input("Enter your choice (1-8): "))
     except ValueError:
        print("Invalid input. Please enter a number.")
        continue
     if choice==1:
            add_expense()
     elif choice==2:
            view_expenses()
     elif choice==3:
            delete_expense()
     elif choice==4:
            update_expense()
     elif choice==5:
            filter_expenses()
     elif choice==6:
            category_summary()
     elif choice==7:
            save_and_exit()
     elif choice==8:
            search()
     if choice<1 or choice>8:
      print("Invalid choice. Please try again.")
     again = input("\nDo you want to track more expenses? (yes/no): ")

     while True:
         if again.lower() == "yes":
             break
         elif again.lower() == "no":
             save_and_exit()
         else:
             print("Invalid input. Please enter 'yes' or 'no'.")
             again = input("\nDo you want to track more expenses? (yes/no): ")