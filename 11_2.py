class LimitExceedException(Exception):
    def __init__(self,arg):
        self.msg=arg

class InvalidMinimumException(Exception):
    def __init__(self,arg):
        self.msg=arg

class InsufficientFundException(Exception):
    def __init__(self,arg):
        self.msg=arg

class Bank_account: 
    def __init__(self): 
        self.balance=0
  
    def deposit(self):
        amount=int(input("Enter amount to be Deposited: "))
        if amount > 10000:
            raise LimitExceedException("Limit Exceeded. Please enter amount less than 10000")
        elif amount < 100:
            raise InvalidMinimumException("Please enter amount greater than 100")
        else:
            self.balance += amount
            print("Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = int(input("Enter amount to be Withdrawn: ")) 
        if amount > 10000:
            raise LimitExceedException("Limit Exceeded. Please enter amount less than 10000")
        elif amount < 100:
            raise InvalidMinimumException("Please enter amount greater than 100")        
        elif amount > self.balance: 
            raise InsufficientFundException("Enter amount less than balance")
        else:
            self.balance-=amount
            print("Your transaction is being processed") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance)

c = Bank_account()
c.deposit()
c.withdraw()
c.display()