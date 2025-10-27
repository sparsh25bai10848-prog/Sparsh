# Financial Management Application(unfinished)

# Display Menu
def menu():
    print("\n Financial Management ")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

# Storing data
transactions = []

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        amount = float(input("Enter income amount: "))
        category = input("Enter income category: ")
        transactions.append({'type': 'income', 'amount': amount, 'category': category})
        print("Income added.")
    elif choice == '2':
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        transactions.append({'type': 'expense', 'amount': amount, 'category': category})
        print("Expense added.")
    elif choice == '3':
        total_income = 0
        total_expense = 0

    
        for t in transactions:
           if t['type'] == 'income':
            total_income += t['amount']
           elif t['type'] == 'expense':
            total_expense += t['amount']

        balance = total_income - total_expense

        print("\n Summary ")
        print("Total Income: ₹", total_income)
        print("Total Expense: ₹", total_expense)
        print("Remaining Balance: ₹", balance)

    elif choice == '4':
        print("Exiting")
        break
    else:
        print("Invalid choice. Try again.")

