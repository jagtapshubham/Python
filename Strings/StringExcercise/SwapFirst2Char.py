"""Output
Enter string1=abc
Enter string2=xyz
xyc abz

"""

#!/usr/bin/python3

def swap_char(string1,string2):
    char1=string1[:2]
    char2=string2[:2]
    string1=char2+string1[2:]
    string2=char1+string2[2:]
    return string1,string2

if __name__=='__main__':
    string1=input("Enter string1=")
    string2=input("Enter string2=")
    nstr1,nstr2=swap_char(string1,string2)
    print(nstr1,nstr2)

