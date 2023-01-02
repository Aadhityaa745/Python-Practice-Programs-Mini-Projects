# Decimal To Binary
'''
dec = int(input('Enter a Decimal Number :'))
binary = ""
temp = dec
while dec>0:# 45
    rem = dec%2
    binary = str(rem)+binary
    dec//=2

print("Binary of",temp,"is =",binary)
'''
# bin
#print(bin(45))
#print(bin(137))#10001001
#print(hex(140))
#print(oct(48))
# Decimal to Octal
'''
dec = int(input("Enter a number :"))
octal = ""
temp = dec
while dec>0:
    rem = dec%8
    octal = str(rem)+octal
    dec//=8

print ("Octal value of ",temp," is :",octal) 
'''

# Decimal to Hexa
'''
dec = int(input("Enter a Decimal Number :"))
temp = dec
hexa = "0123456789ABCDEF"#
ans = ""
while dec>0:
    rem = dec%16
    ans = hexa[rem]+ans#8C
    dec//=16
print("Hexa =",ans)
        
'''

# Nested Loops

'''
*
* *
* * *
* * * *
'''
#
'''
for a in range(1,5):
    for b in range(1,a+1):
        print('*',end=' ')

    print()

'''

#
'''
* * * *
* * *
* *
*
'''
#
'''
for a in range(5,1,-1):
    for b in range(1,a):
        print("*", end =' ')
    print()
'''
#
'''
for a in range(1,5):
    for b in range(4,a,-1):
        print(' ',end='')
    for c in range(1,a+1):
        print('*',end=' ')
    print()

'''







