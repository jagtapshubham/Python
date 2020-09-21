#!/usr/bin/python3

def main():
    limit=eval(input("Enter size of list="))
    i=0
    array=[]
    num=1
    for i in range(0,limit):
        num=eval(input("Enter number="))
        array.append(num)
    print("List elements:",array)

if __name__=='__main__':
    main()
