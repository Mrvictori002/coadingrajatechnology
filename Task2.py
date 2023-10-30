class Transaction:
    def __init__(self, category, amount, transaction_type):
        self.category = category
        self.amount = amount
        self.transaction_type = transaction_type  # 'expense' or 'income'

import pickle

class BudgetTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.file_path, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def save_transactions(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.transactions, file)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_transactions()

    def calculate_budget(self):
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == 'income')
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == 'expense')
        remaining_budget = total_income - total_expenses
        return remaining_budget

    def categorize_expenses(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction.transaction_type == 'expense':
                category = transaction.category
                amount = transaction.amount
                if category in expense_categories:
                    expense_categories[category] += amount
                else:
                    expense_categories[category] = amount
        return expense_categories

def main():
    file_path = 'transactions.pkl'
    budget_tracker = BudgetTracker(file_path)

    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. View Expense Analysis")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            transaction = Transaction(category, amount, 'income')
            budget_tracker.add_transaction(transaction)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            transaction = Transaction(category, amount, 'expense')
            budget_tracker.add_transaction(transaction)
        elif choice == '3':
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == '4':
            expense_categories = budget_tracker.categorize_expenses()
            print("Expense Analysis:")
            for category, amount in expense_categories.items():
                print(f"{category}: ${amount:.2f}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

