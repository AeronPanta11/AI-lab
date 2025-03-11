dict=(input("please enter key value pair such that k1,v1,k2,v2")).split(",")
dictionary={dict[i]:dict[i+1]for i in range(0,len(dict),2)}
print(f"dictionary is {dictionary}")