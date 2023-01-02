# Palindrome Check in Numbers
# 121 --> 121

num = int(input('Enter Any Number : '))
pal =0
temp = num

while num>0: # 345 --> 543
    mod = num%10 # 5, 4, 3
    pal=pal*10+mod#5, 54, 543
    num//=10 # 34, 3, 0

print(pal)
if pal==temp:
    print('Palindrome')
else:
    print('Not a Palindrome')
