def sNumber():
    studentNumber=[]
    for i in range (1,10):
        print(f"please eneter the number of {i}th student")
        studentNumber.append(input())
    return studentNumber
marks=sNumber()
for index,mark in enumerate (marks):
    print(f"The marks of {index+1} student is {mark}")
    
