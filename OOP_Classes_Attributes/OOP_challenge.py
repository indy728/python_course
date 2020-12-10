class Account:

    def __init__(self,owner,balance=0.00):
        self.owner = owner
        self.balance = balance

    def deposit(self, credit):
        self.balance += credit
        print("Deposit accepted.")

    def withdraw(self, debit):
        if (debit > self.balance):
            print(f"Your attempted withdrawal ({debit}) exceeds "\
                    + f"your current available funds ({self.balance}). "\
                    + "No action has been taken.")
        else:
            self.balance -= debit
            print("Withdrawal accepted. Please take your cash.")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

acct1 = Account('Kyle')

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
print(acct1.balance)

acct1.withdraw(75)

acct1.deposit(2335.63)
print(acct1.balance)

acct1.withdraw(75)
print(acct1.balance)
