"""
output1
Enter string=add
adding

output2
Enter string=adding
addingly
"""

#!/usr/bin/python3

def adding_ing(string):
    x=string.endswith('ing',-3)     #check whether string ends with 'ing' if yes then add 'ly' to string 
    if x==True:
        string=string+'ly'
        return string
    else:                           #if string doesn't end with 'ing' then add 'ing'
        string=string+'ing'
        return string

if __name__=='__main__':
    string=input("Enter string=")
    if len(string)<3:              # if string length is less than 3 than leave it unchange
        print(string)
    else:
        modified_string=adding_ing(string)
        print(modified_string)

