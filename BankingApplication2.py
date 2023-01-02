# Banking Application

dic = {1:{'name':'Aadhitya','pin':1234,'balance':20000},2:{'name':'Lavanya','pin':4567,'balance':10000}}

def show():
    print('*********************')
    print('Welcome to ABC Bank ')
    print('*********************')
    pinno = int(input('\nEnter Pin number :'))
    '''
    pin = dic[1]['pin']
    if pin==pinno:
        print('\nWelcome ',dic[1]['name'])
        key = 1
        show2(key)
    elif dic[2]['pin']==pinno:
        print('\nWelcome ',dic[2]['name'])
        key = 2
        show2(key)
    else:
        print('\nEnter Valid Pin Number :')
    '''
    for a in dic:
        for b in dic[a]:
            if dic[a]['pin']==pinno:
                print('Welcome',dic[a]['name'])
                show2(a)
                break
    else:
        print('Invalid PIN Number')
            
def show2(key):
    print('\nEnter the mode of option that you want ')
    print('\n1. Withdraw 2. Deposit 3. Balance ')
    opt = int (input())
    if opt==1:
        withdraw(key)
    elif opt==2:
        deposit(key)
    elif opt==3:
        balance = dic[key]['balance']
        print('Your balance is : ',balance)
    else:
        print('Invalid Option!')

def withdraw(key):
    print('Enter the amount to be withdrawn : ')
    amount = int (input())
    dic[key]['balance']-=amount
    print('Balance is : ',dic[key]['balance'])

def deposit(key):
    print('Enter the amount to be deposited : ')
    amount = int (input())
    dic[key]['balance']+=amount
    print('Balance is : ',dic[key]['balance'])
show()      
