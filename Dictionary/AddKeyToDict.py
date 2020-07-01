#!/usr/bin/python3

def main():
    dict1=dict()
    ch=1
    while(ch!=0):
        key=input("Enter key=")
        value=input("Enter value=")
        dict1[key]=value
        ch=eval(input("Enter ch (exit/0)="))
    print(dict1)

if __name__=='__main__':
    main()
