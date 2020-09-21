"""Output
Programming
"""

#!/usr/bin/python3

def longest_word_length(*args):     # *args is used to take variable number of arguments
    max=0
    for x in args:
        a=len(x)                #a is used to store length of string for comparision
        if a>max:               
            max=a
            st=x                #st is used to store the longest string
        else:
            continue
    return st

if __name__=='__main__':
    length=longest_word_length("Hello","Welcome","To","Programming")
    print(length)
