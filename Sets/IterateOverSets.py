#!/usr/bin/python3

def main():
    n=5
    s=set()
    for i in range(n):
        x=eval(input("Enter number="))
        s.add(x)
    for i in s:
        print(i)

if __name__=='__main__':
    main()
