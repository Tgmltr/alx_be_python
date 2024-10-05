class BankAccount:
    def __init__(self, account_ballance):
        self.account_ballance = account_ballance
        #self.account_ballance=0

    def deposit(self,amount):
        self.account_ballance += amount

    def withdraw(self,amount):
        if amount<=self.account_ballance:
            self.account_ballance -= amount
            return True
        else: return False

    def display_balance(self):
        print("Current Balance:",self.account_ballance)
