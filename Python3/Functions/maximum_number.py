#!/usr/bin/python3

def max_num(a,b,c):
    if a>b and a>c:
        print("%d is Maximum number"%a)
    elif b>c:
        print("%d is Maximum number"%b)
    else:
        print("%d is Maximum number"%c)

def main():
    a,b,c=eval(input("Enter a,b,c="))
    max_num(a,b,c)

if __name__=='__main__':
    main()
