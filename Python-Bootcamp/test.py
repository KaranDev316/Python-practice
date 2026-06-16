#exercise 4: Bank Account

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"You have received ${amount}  and your balance is ${self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn ${amount}  and your balance is ${self.balance}")
        else:
            print(f"Sorry, you have insufficient balance")
    def get_balance(self):
        return self.balance


alfred = BankAccount(100)

print(f"Your account balance is {alfred.get_balance()}")
