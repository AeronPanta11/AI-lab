class bank_account:
    def __init__(self):
        self.__bankBalance=float(input("please enter the initial balance"))
        self.__acountNumber=input("please enter the account number")
    def deposit(self):
        self.__bankBalance=self.__bankBalance+float(input("Deposit Amount"))
    def withDraw(self):
        self.__bankBalance=self.__bankBalance-float(input("please enter the withdrawl amount"))
    def getBalance(self):
        print(f"The current balance is {self.__bankBalance}")
Ram=bank_account()
Ram.deposit()
Ram.withDraw()
Ram.getBalance()

