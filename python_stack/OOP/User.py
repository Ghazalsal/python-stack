class User:

    def __init__(self,name,balance=1):
        self.name=name
        self.balance=balance

    def make_withdrawal(self,amount):
        if (amount <= self.balance):
            self.balance=self.balance-amount

    def displayinfo(self):
        print(f"User name is: {self.name}")
        print(f"Account balance: {self.balance}$")

    def deposite(self,amount):
        self.balance=self.balance + amount

user1 = User("Jad",500)
user2 = User("Mohammed",200)
user3 =User("Ali")


user1.deposite(100)
user1.deposite(100)
user1.deposite(150)
user1.make_withdrawal(50)

user1.displayinfo()


