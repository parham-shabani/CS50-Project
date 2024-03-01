import time

budget = {}
def add_month_budget(month):
    income = float(input("Enter income for {}: ".format(month)))
    expenses = float(input("Enter expenses for {}: ".format(month)))
    savings = income - expenses
    print("")

    budget[month] = {
        "income": income,
        "expenses": expenses,
        "savings": savings
    }

def display_month_budget( month):
    if month in budget:
        print("Budget for", month)
        print("Income:", budget[month]["income"])
        print("Expenses:", budget[month]["expenses"])
        print("Savings:", budget[month]["savings"],"\n")
    else:
        print("Budget for", month, "not found.\n")

def calculate_total_savings():
    total_savings = sum(budget[month]["savings"] for month in budget)
    print("Total savings:", total_savings,"\n")

def main():
    while True:
        time.sleep(3)
        print("1. Add month budget")
        print("2. Display month budget")
        print("3. Calculate total savings")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            month = input("Enter the month: ")
            add_month_budget(month)
        elif choice == "2":
            month = input("Enter the month: ")
            display_month_budget(month)
        elif choice == "3":
            calculate_total_savings()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
