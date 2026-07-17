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
            print("5. Final Balance")
            print("6. Update Transaction")
            print("7. Delete Transaction")
            print("8. Exit")
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
                print(f"The Final Balance is {self.show_current_balance()}")
            elif choice == 6:
                self.update_transaction()
            elif choice == 7:
                self.delete_transaction()   
            elif choice == 8:
                print("Goodbye")
                break    
            else:
                print("Enter Valid Choice")

    def delete_transaction(self):
        self.view_transactions()
        try:
            idd = int(input("Enter the Transaction ID to Delete: "))
        except ValueError:
            print("Please enter a valid ID.")
            return

        self.cursor.execute(
            "Select * from Transactions where id = ?",
            (idd,)
        )
        transaction = self.cursor.fetchone()
        if transaction is None:
            print("Transaction is not found.")
            return

        self.cursor.execute('''
                        Delete from Transactions
                        Where id = ?
                        ''', (idd,)
                        )
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Transaction Deleted Successfully.")
        else:
            print("Transaction deletion unsuccessful.")
    
    def update_transaction(self):
        self.view_transactions()

        try:
            idd = int(input("Enter the Transaction ID to update: "))
        except ValueError:
            print("Please enter a valid ID.")
            return

    # Check whether the transaction exists
        self.cursor.execute(
            "SELECT * FROM Transactions WHERE id = ?",
            (idd,)
        )
        
        transaction = self.cursor.fetchone()

        if transaction is None:
            print("Transaction not found.")
            return

        try:
            newdate = input("Enter the new Date: ")
            newdescription = input("Enter the new Description: ")
            newcategory = input("Enter the new Category: ")
            newamount = float(input("Enter the new Amount: "))
            new_transaction_type = input("Enter the new Transaction Type (Income/Expense): ")
        except ValueError:
            print("Please enter valid values.")
            return

        updated_transaction = (
            newdate,
            newdescription,
            newcategory,
            newamount,
            new_transaction_type,
            idd
        )

        self.cursor.execute(
            '''
            UPDATE Transactions
            SET
                Date = ?,
                Description = ?,
                Category = ?,
                Amount = ?,
                Type = ?
            WHERE id = ?
            ''',
            updated_transaction
        )

        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("Transaction updated successfully!")
        else:
            print("Transaction could not be updated.")

    def show_current_balance(self):
        tot_income = self.show_total_income()
        tot_expense = self.show_total_expense()
        return tot_income - tot_expense


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