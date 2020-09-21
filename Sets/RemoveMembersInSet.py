#!/usr/bin/python3

def main():
    s=(['one','two','three','four','five'])
    print(s)
    x=input("Enter element to remove=")
    s.remove(x)
    print(s)

if __name__=='__main__':
    main()
