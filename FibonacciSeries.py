def fibonacci(n):
    if n<=1:
        return n
    else :
        return(fibonacci(n-1)+fibonacci(n-2))
    
'''nterms = 10'''
nterms = int(input("Enter no. of terms : "))
if nterms<=0:
    print("Enter a positive number!!!")
else:
        print("Fibonacci sequence ")
        for i in range(nterms):
            print(fibonacci(i))
