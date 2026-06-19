while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please Enter valid value")
        continue
    if(choice == 1):
        try:
            expense = int(input("Enter Expense: "))
        except ValueError:
            print("Enter Valid Value")
            continue
        with open('expense.txt', 'a') as file:
            file.write(f"{expense}\n")
        print(f"The Expense added is {expense}")
    elif(choice == 2):
        try:
            with open('expense.txt', 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No Expense has been saved yet!!")
    elif(choice == 3):
        
        print("Goodbye")
        break
    else:
        print("Invalid Choice")