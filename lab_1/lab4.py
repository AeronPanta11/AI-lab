from math import sqrt,ceil
def primecalc(n1,n2):
    
    b=[]
    for i in range (n1,n2):
        a=1
        for j in range (1,int(i/2)):
            if i%(j+1)==0:
                a=0
                continue
        if a==1:
            b.append(i)
            
    return b
print("this code will find the prime number between n1 and n2")
n1=int(input("pleaase enter the first number"))
n2=int(input("pleaase enter the second number"))
p=primecalc(n1,n2)
print(p)