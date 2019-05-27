class WithdrawalError(Exception):
    pass
class DepositError(Exception):
    pass

class Savingsaccount:
    def __init__(self,b=500):
        try:
            if b<500:
                raise DepositError
            else:
                self.bal=b
                print("Account deposited Available balance is",self.bal,"\n")
        except DepositError:
            print("Minimum amount of 500 should be deposit.Please deposit amount greater than 500\n" )
            del(self)
    def deposit(self,a):
        self.bal+=a
        print("Amount deposited is Rs.",a,"Available balance :Rs",self.bal,"\n")

    def withdrawal(self,x):
        try:
            if x>self.bal:
                raise WithdrawalError
            else:
                self.bal-=x
                print("Amount withdrawn is Rs.",x,"Available balance: Rs.",self.bal,"\n")
        except WithdrawalError:
            print("Withdrawal amount exceeds available balance.\n")

u=Savingsaccount(400)
u=Savingsaccount(1000)
u.deposit(5000)
u.withdrawal(10000)
u.deposit(1000)
u.withdrawal(542)