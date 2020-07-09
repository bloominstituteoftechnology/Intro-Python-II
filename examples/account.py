class Account:
    interest = 0.02
    def __init__(self, holder):
        self.balance = 10000
        self.holder = holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return f'Insufficient funds :( you currently have ${self.balance}'
        self.balance -= amount
        return f'New balance: ${self.balance}'

my_account = Account('Gavin')
sean_account = Account('Sean')