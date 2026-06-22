def show_total_expense():
    total = 0
    try:
        with open('expense.txt', 'r') as file:
            for line in file:
                expense, category, description = line.strip().split(',')
                total += int(expense)
    except FileNotFoundError:
        print("No File Found!!")
        
    return total

def add_expense():
    try:
        expense = int(input("Enter Expense: "))
        category = input("Enter the category: ")
        description = input("Enter the description: ")
    except ValueError:
        print("Enter Valid Value")
        return
    with open('expense.txt', 'a') as file:
        file.write(f"{expense},{category},{description}\n")
        print(f"The expense added is {expense}")
        print(f"The category added is {category}")
        print(f"The description added is {description}")

def view_expenses():
    try:
        with open('expense.txt', 'r') as file:
            for line in file:
                expense, category, description = line.strip().split(',')
                print(f"The expense is {expense}")
                print(f"The category is {category}")
                print(f"The description is {description}")
                print('-' * 20)
    except FileNotFoundError:
        print("No Expense has been saved yet!!")
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total Expense")
    print("4. Exit")
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please Enter valid value")
        continue
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        print(f"The Total Expenses are {show_total_expense()}")
    elif choice == 4:
        
        print("Goodbye")
        break
    else:
        print("Invalid Choice")