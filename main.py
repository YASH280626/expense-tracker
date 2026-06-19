while True:
    print("1. Add Expense")
    print("2. Exit")
    choice = int(input("Enter Your Choice: "))
    if(choice == 1):
        expense = int(input("Enter Expense: "))
        with open('expense.txt', 'a') as file:
            file.write(f"{expense}\n")
        print(f"The Expense added is {expense}")
    elif(choice == 2):
        print("Goodbye")
        break
    else:
        print("Invalid Choice")