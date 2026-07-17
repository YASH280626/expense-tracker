import sqlite3
connection = sqlite3.connect('expense.db')
cursor = connection.cursor()
# Creating the Table
cursor.execute('''
    Create Table If Not Exists Transactions(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Date Text,
               Description Text,
               Category Text,
               Amount Real,
               Type Text)''')
connection.commit()
class ExpenseTracker:

    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def run(self):
        while True:
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Show Total Expenses")
            print("4. Show Total Income")
            print("5. Exit")
            try:
                choice = int(input("Enter Your Choice: "))
            except ValueError:
                print("Please Enter Valid Value")
                continue
            if choice == 1:
                self.add_transaction()
            elif choice == 2:
                self.view_transactions()
            elif choice == 3:
                print(f"The Total Expenses are {self.show_total_expense()}")
            elif choice == 4:
                print(f"The Total Income is {self.show_total_income()}")
            elif choice == 5:
                print("Goodbye")
                break
                
            else:
                print("Enter Valid Choice")

    def show_total_expense(self):
        self.cursor.execute('''Select SUM(Amount)
                       from Transactions
                       where Type = 'Expense'
                    ''')
        total = self.cursor.fetchone()
        if total[0] is None:
            return 0
            
        return total[0]

    def show_total_income(self):
        self.cursor.execute('''Select SUM(Amount)
                        from Transactions
                        where Type = 'Income'
                    ''')
        total = self.cursor.fetchone()
        if total[0] is None:
            return 0
        return total[0]

    def add_transaction(self):
        try:
            date = input("Enter the Date of transaction: ")
            amount = float(input("Enter the Amount: "))
            transaction_type = input("Enter the Type of transaction: ")
            
            category = input("Enter the category: ")
            description = input("Enter the description: ")
        except ValueError:
            print("Enter Valid Value")
            return
        transaction_data = (date, description, category, amount, transaction_type)
        self.cursor.execute(''' 
            Insert Into Transactions(Date, Description, Category, Amount, Type)
                       values(?, ?, ?, ?, ?)
            ''', transaction_data)
        self.connection.commit()

    def view_transactions(self):
        self.cursor.execute('Select * from Transactions')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

tracker = ExpenseTracker(connection, cursor)
tracker.run()