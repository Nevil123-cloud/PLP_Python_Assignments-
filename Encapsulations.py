class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance is {self.__balance}.")
        else:
            print("Insufficient balance.")

account = BankAccount("123456789", 1000)
account.deposit(500)  
account.withdraw(300)  
