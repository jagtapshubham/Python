#!/usr/bin/python3

def replace_char(string,char):
    string=string.replace(char,'$')
    string=string.replace('$',char,1)
    return string

if __name__=='__main__':
    string=input("Enter string=")
    char=input("Enter character to replace=")
    new_string=replace_char(string,char)
    print(new_string)

