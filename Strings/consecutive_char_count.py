#!/usr/bin/python3

def consecutive_char(string):
    string2=""
    count=0
    a=string[0]
    for i in string:
        if i is a:
            count+=1
        else:
            if count>1:
                string2=string2+a+str(count)
            else:
                string2=string2+a
            a=i
            count=1
    else:                                       # this else executes when above for loop is completely excuted
        if count>1:
            string2=string2+a+str(count)
        else:
            string2=string2+a

    print(string2)

def main():
    string=input("Enter string=")
    consecutive_char(string)

if __name__=='__main__':
    main()
