#!/usr/bin/python3

def First_Last_2_Char(string):
    if len(string)<2:
        return""
    else:
        return string[0:2],string[-2:]

if __name__=='__main__':
    string=input("Enter string=")
    first,last=First_Last_2_Char(string)
    print(first)
    print(last)
