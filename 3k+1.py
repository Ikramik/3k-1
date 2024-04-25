n = input ("get a number")
n = int (n)
if n>1000:
    print("error")
else:
    while (n>1):
        if n%2==0 :
            n=n/2
            print(n)
        elif n%2!=0 :
            n=3*n+1
            print (n)
    
