#!/usr/bin/python3

def convert_upper_lower(string):
    if string.islower():
        string=string.upper()
    else:
        string=string.lower()
    print(string)

if __name__=='__main__':
    string=input("Enter String=")
    convert_upper_lower(string)
