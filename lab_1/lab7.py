def word_numbers(sent):
    count=1
    for letter in sent:
        if len(sent)==0:
            count=0
        elif letter==" ":
            count+=1
    return count
print(f"The number of words in sentence is {word_numbers(input("please enter the sentence: "))}")