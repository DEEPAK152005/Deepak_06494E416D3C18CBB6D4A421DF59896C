class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
        self.__minimum_balance = 500.0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance:.2f}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance - amount >= self.__minimum_balance:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance:.2f}")
            else:
                print("Insufficient balance. Need a minimum balance of $500 to withdraw.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}")

account = BankAccount("12345", "John Doe", 1000.0)

while True:
    print("\nMenu:")
    print("1. Withdraw cash")
    print("2. Deposit money")
    print("3. Exit Atm")
    choice = input("Enter your choice: ")

    if choice == '1':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(withdraw_amount)
    elif choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: "))
        account.deposit(deposit_amount)
    elif choice == '3':
        print("No Free Money.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1, 2, or 3).")
