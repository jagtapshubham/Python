"""Output
dbca
"""

#!/usr/bin/python3

def exchange_char(string):
    first_char=string[:1]
    last_char=string[-1:]
    string=last_char+string[1:]
    string=string[:-1]+first_char
    return string

if __name__=='__main__':
   print(exchange_char("abcd"))         # input string
