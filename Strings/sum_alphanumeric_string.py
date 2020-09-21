#!/usr/bin/python3

def sum_alphanumeric(alpha_string):
    res=0
    for i in alpha_string:
        if i.isdigit():             # isdigit function is used to check i is digit or not
            res+=int(i)             # i is string so it is converted to integer
    return res

def main():
    res=0
    alpha_string=input("Enter alphanumeric string=")
    res=sum_alphanumeric(alpha_string)
    print(res)

if __name__=='__main__':
    main()
