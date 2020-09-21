#!/usr/bin/python3

def min_number(a,b,c):
    if a<b and b<c:
        print("%d is minimum number"%a)
    elif b<c:
        print("%d is minimum number"%b)
    else:
        print("%d is minimum number"%c)

def main():
    min_number(10,5,50)

if __name__=='__main__':
    main()
