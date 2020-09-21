#!/usr/bin/python3

def change_char(string):
    char=string[0]
    string=string.replace(char,'$')
    string=char+string[1:]

    return string

if __name__=='__main__':
    string=input("Enter string=")
    new_string=change_char(string)
    print(new_string)

