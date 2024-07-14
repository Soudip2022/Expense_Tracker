def add_expense(expenses):
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category (e.g., groceries, transport, entertainment): ")
    description = input("Enter a brief description: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    
    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    
    expenses.append(expense)
    print("Expense added successfully!")

def list_expenses(expenses):
    for expense in expenses:
        print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

categories = {"groceries", "transport", "entertainment", "utilities", "miscellaneous"}

from datetime import datetime

def calculate_total(expenses, start_date, end_date):
    total = 0
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    for expense in expenses:
        date = datetime.strptime(expense['date'], "%Y-%m-%d")
        if start <= date <= end:
            total += expense['amount']
    
    print(f"Total expenses from {start_date} to {end_date}: {total}")

def monthly_report(expenses, month):
    report = {}
    for expense in expenses:
        expense_month = expense['date'][:7]
        if expense_month == month:
            category = expense['category']
            report[category] = report.get(category, 0) + expense['amount']
    
    print(f"Monthly Report for {month}:")
    for category, total in report.items():
        print(f"{category}: {total}")

def save_data(expenses, filename="expenses.txt"):
    with open(filename, "w") as file:
        for expense in expenses:
            line = f"{expense['date']},{expense['amount']},{expense['category']},{expense['description']}\n"
            file.write(line)
    print("Data saved successfully!")

def load_data(filename="expenses.txt"):
    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                date, amount, category, description = line.strip().split(',')
                expenses.append({
                    "date": date,
                    "amount": float(amount),
                    "category": category,
                    "description": description
                })
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found.")
    
    return expenses

def main():
    expenses = load_data()
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Calculate total expenses")
        print("4. Generate monthly report")
        print("5. Save data")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            list_expenses(expenses)
        elif choice == '3':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            calculate_total(expenses, start_date, end_date)
        elif choice == '4':
            month = input("Enter the month (YYYY-MM): ")
            monthly_report(expenses, month)
        elif choice == '5':
            save_data(expenses)
        elif choice == '6':
            save_data(expenses)  # Auto-save before exit
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
