class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
    
    def check_balance(self):
        return self.balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(200)  
print(account.check_balance())  





















# The BankAccount class manages a balance, with methods to deposit
# , withdraw, and check the balance.