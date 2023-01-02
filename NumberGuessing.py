#

import random

randomNumber = random.randrange(1,10)

'''
userNumber = int(input('Enter Any Number between 1 and 10 :'))

if userNumber == randomNumber:
    print('You win')
else:
    print('You lose')

    print('The Random Number is =',randomNumber)
'''
# For loop
'''
for a in range(3):
    userNumber = int(input("Enter Any Number between 1 and 10 : "))
    if userNumber==randomNumber:
        print('You Win')
        break
    else:
        print('You Lose')

print('The Random Number is :',randomNumber)
'''

# 
'''
if randomNumber%2==0:
    clue1 = "It is an even number"
else:
    clue1 = "It is an Odd number"

if randomNumber%3==0:
    clue2="It is divisible by 3 without reminder"
elif randomNumber%4==0:
    clue2="It is divisible by 4 without reminder"
else:
    clue2= "It is a prime Number"
    
userNumber = int(input('Enter Any Number between 1 and 10 :'))

if randomNumber == userNumber:
    print('You Win!')
else:
    print('Wrong Answer')
    print('Clue : ',clue1)

    userNumber = int(input('Enter Any Number between 1 and 10 :'))
    if userNumber == randomNumber:
        print('You Win!')
    else:
        print('Wrong Answer')
        print('Clue : ',clue2)
        userNumber = int(input('Enter Any Number between 1 and 10 :'))
        if userNumber == randomNumber:
            print('You Win!')
        else:
            print('You Lose!')
            print('The Random Number is:',randomNumber)

'''

