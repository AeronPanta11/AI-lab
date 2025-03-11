def count_chr(sen):
    count_dict={}
    for char in sen:
        if char in count_dict.keys():
            count_dict[char]+=1
        else:
            count_dict[char]=1
    return count_dict
sen=input("please enter the sentence.")
print(f"The count of each character in sentence is {count_chr(sen)}")