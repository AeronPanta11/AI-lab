def Rfun(a):
    sum=0
    greatest=0
    a=[int(i) for i in a]
    for i in a:
        sum=sum+i
        if greatest<i:
            greatest=i
    return sum,greatest
tup=Rfun([float(i) for i in (input("please enter the list")).split()])
print(tup[0])
print(tup[1])