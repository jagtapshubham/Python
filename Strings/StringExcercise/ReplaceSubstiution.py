"""Output
Enter string=lyrics is not that poor
lyrics is good
"""

#!/usr/bin/python3

def string_substiution(string):
    snot=string.find('not')
    spoor=string.find('poor')

    if spoor>snot and snot>0 and spoor>0:
        string=string.replace(string[snot:(spoor+4)],'good')
        return string
    else:
        return string

if __name__=='__main__':
    string=input("Enter string=")
    new_string=string_substiution(string)
    print(new_string)

