from abc import *
'''
each bank will have account,
and every account can withdraw and deposit money from atm
for withdraw, must have a sufficient money in account
'''
class Account(metaclass=ABCMeta):
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, money):
        self._balance = money

    @abstractmethod
    def withdraw(self, money):
        print("Hi, You are tring to withdraw money")

    @abstractmethod
    def deposit(self, money):
        print("Hi, You are trying to deposit money")

    @abstractmethod
    def __str__(self):
        pass
class CheckingAcoount(Account):
    def __init__(self):
        #Account.__init__(self)
        self.name = "check"
    def withdraw(self, money):
        try:
            money > self.balance
        except:
            print("Insufficient money in account")
        else:
            self.balance -= money

    def deposit(self, money):
        self.balance+=money

    def __str__(self):
        return "account balance: {0}, and account type: {1}".format(self.balance, self.name)


if __name__ == '__main__':
    a = CheckingAcoount()
    a.balance = 100
    print(a)
    a.balance += 100
    print(a)