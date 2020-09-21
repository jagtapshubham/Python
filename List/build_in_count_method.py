#!/usr/bin/python3

def main():
    array=[]
    i=0
    size=eval(input("Enter size of list="))
    while i<size:
        num=eval(input("Enter element="))
        array.append(num)
        i+=1
    print(array)
    key=eval(input("Enter key="))
    print(array.count(key))

if __name__=='__main__':
    main()

