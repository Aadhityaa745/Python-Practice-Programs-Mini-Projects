# Banking App ---> 1. Withdraw, 2. Deposit, 3. Balance Enq, 4. Change PIN
'''
dic = {'name':'Aadhitya','pin':1234,'balance':20000}

def show():
    print('----------------------------------------------------------')
    print('Welcome to ABC Bank')
    print('----------------------------------------------------------')
    p = int(input('Enter PIN Number : '))
    if p==dic['pin']:
        print('\nWelcome',dic['name'])
        show2()
    else:
        print('\nInvalid PIN Number!')

def show2():
    print('\nSelect Any Option')
    print('\n1. Withdraw      2. Deposit    \n3. Balance Enquiry    4. Change PIN Number')
    opt = int(input())
    check(opt)
    
def check(o):
    if o==1:
        withdraw()
    elif o==2:
        deposit()
    elif o==3:
        print('\nYour Balance is : ',dic['balance'])
    elif o==4:
        change()

def withdraw():
    amount = int(input('\nEnter the Amount to be Withdrawn : '))
    if amount<dic['balance']:
        dic['balance']-=amount
        print('\nYour Transaction is Successfull')
        print('\nBalance Amount = ',dic['balance'])
    else:
        print('\nInsufficient Balance! Enter the amount within',dic['balance'])
        withdraw()

def deposit():
    amount = int(input('\nEnter the Amount to be Deposited : '))
    dic['balance']+=amount
    print('\nDeposited Successfully')
    print('\nBalance Amount = ',dic['balance'])

def change():
    op = int(input('\nEnter Old PIN Number : '))
    if op==dic['pin']:
        np = int(input('\nEnter New PIN Number : '))
        dic['pin']= np
        print('\nYour PIN Number has been changed Successfully!')
    else:
        print('\nInvalid PIN Number!')
        
for a in range(10):    
    show()
'''

dic = {1:{'name':'Aadhitya','pin':1234,'balance':20000},2:{'name':'Lavanya','pin':4567,'balance':10000}}








