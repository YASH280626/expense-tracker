class ExpenseTracker:

    def __init__(self):
        self.filename = 'expense.txt'

    def run(self):
        while True:
            print("1. Add Expense")
            print("2. View Expense")
            print("3. Show Total Expenses")
            print("4. Exit")
            try:
                choice = int(input("Enter Your Choice: "))
            except ValueError:
                print("Please Enter Valid Value")
                continue
            if choice == 1:
                self.add_expense()
            elif choice == 2:
                self.view_expenses()
            elif choice == 3:
                print(f"The Total Expenses are {self.show_total_expense()}")
            elif choice == 4:
                print("GoodBye!!")
                break
            else:
                print("Enter Valid Choice")


    def show_total_expense(self):
        total = 0
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    expense, category, description = line.strip().split(',')
                    total += int(expense)
        except FileNotFoundError:
            print("No File Found!!")
            
        return total

    def add_expense(self):
        try:
            expense = int(input("Enter Expense: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
        except ValueError:
            print("Enter Valid Value")
            return
        with open(self.filename, 'a') as file:
            file.write(f"{expense},{category},{description}\n")
            print(f"The expense added is {expense}")
            print(f"The category added is {category}")
            print(f"The description added is {description}")

    def view_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    expense, category, description = line.strip().split(',')
                    print(f"The expense is {expense}")
                    print(f"The category is {category}")
                    print(f"The description is {description}")
                    print('-' * 20)
        except FileNotFoundError:
            print("No Expense has been saved yet!!")

tracker = ExpenseTracker()
tracker.run()