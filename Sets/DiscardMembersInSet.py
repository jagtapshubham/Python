#!/usr/bin/python3

def main():
    s=set('shubham')#s=set(['s','h','u','b','h','a','m'])
    print(s)
    x=input("Enter element to discard=")
    s.discard(x)
    print(s)

if __name__=='__main__':
    main()
