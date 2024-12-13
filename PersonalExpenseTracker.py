import tabulate as tbl
import pandas as pd
from datetime import datetime
#Add Expense
my_expense = []
def add_expense():
    date_of_expense = validate_date()
    category = input("Please enter category of travel ex- Food or Travel")
    amount = validate_amount("Enter expense amount")
    description = input("Please enter description for expense")
    expense = {
        "date" : date_of_expense,
        "category" : category,
        "amount" : amount,
        "description" : description
    }
    my_expense.append(expense)

def validate_date():
    while True:
        try:
            result = input("Enter date in YYYY-mm-dd format")
            result = datetime.strptime(result, '%Y-%m-%d')
            return result
        except Exception :
            print("Enter Date in the format mentioned")


def validate_amount(msg):
    while True:
        try:
            result = float(input(msg))
            return result
        except Exception :
            print("Enter valid amount")


#view All Expenses
def view_expense():
    try:
        print("Your expense are as below:")
        header = my_expense[0].keys()
        rows =  []
        for x in my_expense:
            if x["amount"] and x["category"]  and x["date"] and x["description"]:
                rows.append(x.values())
            else:
                print("You have invalid date stored as ", x.values())
        print(tbl.tabulate(rows, header))
    except Exception as err:
        print("Error reading list ", err)

#track and set budget
def track_budget():
    total_budget = validate_amount("Enter total budget allocated for month")
    total_expense = calculate_total_expense()
    if total_budget > total_expense:
        print(f"You have { total_budget -  total_expense} left")
    else:
        print(f"You have exceeded your budget by {total_expense - total_budget}")


#save * load Budget
def save():
    df = pd.DataFrame(my_expense)
    df.to_csv('MyExpense.csv')


def load():
    try:
        global my_expense
        df = pd.read_csv('MyExpense.csv', index_col=0)
        my_expense = df.to_dict('records')
    except Exception as err:
        print("Unable to read fiel MyExpense.csv. Please make sure file is present")


def calculate_total_expense():
    total = 0
    for x in my_expense:
        if x["amount"]:
            total+=x["amount"]
    return total

#Display Menu
def displayMenu():
    '''
    o If the user selects option 1, call the function to add an expense
    o If the user selects option 2, call the function to view expenses
    o If the user selects option 3, call the function to track the budget
    o If the user selects option 4, call the function to save expenses to the file
    o If the user selects option 5, save the expenses and exit the program'''
    
    print("\nWelcome to Expense Tracker App")
    while(True):
        try:
            print("Select from choices below")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Track Budget")
            print("4. Save Expenses")
            print("5. Exit")
        
            choice = int(input("Please select a choice from above"))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expense()
            elif choice == 3:
                track_budget()
            elif choice == 4:
                save()
            elif choice == 5:
                save()
                break
            else:
                print("Invalid choice ")
        except Exception :
            print("Invalid choice ")

            
        

load()
displayMenu()

