def sort(n):
    for i in range(len(n)):
        for j in range(len(n) - 1 - i):
            if n[j] > n[j + 1]:
                temp = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp
    return n
n=input("enter the list")
n=[float(i) for i in n.split()]#we have to conver simple string into its individual element before type casting
sorted_list=sort(n)
print(sorted_list)