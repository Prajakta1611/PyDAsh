# program to create a class of bank and get all user info

class Bank:
    """ This is bank class which contain all info about the perticular bank holder."""
    def __init__(self,name:str,acno:int,balance:int):
        self.name = name
        self.acno = acno
        self.__balance = balance
    def info(self):
        """ This Function contain all the info about the bank holder"""
        print("Account holder name :",self.name)
        print("Account Number :",self.acno)
        print("Saving Balance :",self.__balance)
    def deposit(self,amount:int):
        """ This function contain deposite status of the holder"""
        self.__balance += amount
        print("Your updated balance is :",self.__balance)
    def withdrawal(self,amount:int):
        """ This function contain withdrawal status of the holder"""
        self.__balance -= amount
        print("withdrawal amount is :",self.__balance)
b = Bank("ovi",12345,20000)
b.info()
b.deposit(100)
b.withdrawal(500)