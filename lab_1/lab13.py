def reverse(sen):
    reversed=""
    for letter in sen:
        if ord(letter)<91 and ord(letter)>64:
            reversed+=chr(ord(letter)+32)
        elif ord(letter)>90 and ord(letter)<122:
            reversed+=chr(ord(letter)-32)
        else:
            reversed+=letter
    
    return reversed
print(f"the reversed string is { reverse(input("please enter the string"))}")