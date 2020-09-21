#!/usr/bin/python3

def string_length(string):
    count=0
    for i in string:
        count+=1
    return count

if __name__=='__main__':
    string=input("Enter string=")
    count=0
    count=string_length(string)
    print("Length of the String is %d"%count)
