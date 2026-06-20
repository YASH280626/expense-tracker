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
            category = input("Enter the category: ")
            description = input("Enter the descriptioin: ")
        except ValueError:
            print("Enter Valid Value")
            continue
        with open('expense.txt', 'a') as file:
            file.write(f"{expense},{category},{description}\n")
        print(f"The Expense added is {expense}")
        print(f"The category added is {category}")
        print(f"The descriptioin added is {description}")
    elif(choice == 2):
        try:
            with open('expense.txt', 'r') as file:
                for line in file:
                    expense, category, description = line.strip().split(',')
                    print(f"The expense is {expense}")
                    print(f"The category is {category}")
                    print(f"The description is {description}")
                    print("-" * 20)
        except FileNotFoundError:
            print("No Expense has been saved yet!!")
    elif(choice == 3):
        
        print("Goodbye")
        break
    else:
        print("Invalid Choice")