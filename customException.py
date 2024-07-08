class insufficientBalanceException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
balance=int(input('Enter balance amount'))
amount=int(input('Enter withdraw amount'))
try:
    if amount>balance:
        raise insufficientBalanceException('balance not enough')
    else:
        balance=balance-amount
        print('withdraw successful')
        print('withdraw amount=',amount)
        print('balance after withdraw=,',balance)
except insufficientBalanceException as ie:
    print(ie)