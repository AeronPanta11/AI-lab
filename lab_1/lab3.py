a=int(input("enter first number"))
b=int(input("enter se cond numbr"))
def art(a,b):
    return a+b,a-b,a*b,a/b

a=art(a,b)
print(a[0])
print(a[1])
print(a[2])
print(a[3])