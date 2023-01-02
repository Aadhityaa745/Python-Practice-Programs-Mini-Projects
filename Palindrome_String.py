# Palindrome Check in String
'''
word = input('Enter a Word or Sentence : ')
word = word.lower()
# madam --> 5, max index = 4
# abc --> len =3, max_index = 2
pal =""
i = len(word)-1# 4
while i>=0:
    pal+=word[i]# ""+m,m+a=ma,ma+d=mad,mad+a=mada, mada+m=madam,, ""+c=c,c+b=cb,cb+a=cba
    i-=1
    #print(pal)
#print('Reverse :',pal)
if pal==word:
    print('It is a Palindrome Word!')
else:
    print('It is not a Palindrome Word')
'''

# Resume using Format Method, personal details(Name,age,mail-id,place,phone no.,hobbies)
'''
name = input("Enter Name : ")
age = input("Enter Age : ")
place = input("Enter Place : ")
phoneno = input("Enter Phone no. :")
hobbies = input("Enter Hobbies :")
resume = """\n\nPERSONAL DETAILS \n
Name         :     {name}
Age          :     {age}
Place        :     {place}
Phone Number :     {pno}
Hobbies      :     {hob}
"""
print(resume.format(name=name,place=place,age=age,pno=phoneno,hob=hobbies))
'''

