#!/usr/bin/python3

def remove_odd_char(string):
    result=""
    for i in range(len(string)):
        if i%2 == 0:
            result=result+string[i]
    return result

if __name__=='__main__':
    string=input("Enter string=")
    print(remove_odd_char(string))
