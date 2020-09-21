#!/usr/bin/python3

def main():
    list1=list(input("Enter list="))
    print(type(list1))                  # prints type of list1 <class:'list'>
    print(list1)
    list1=tuple(list1)                   # typecasting is done by using tuple(list1)
    print("After type convertion")
    print(type(list1))                  # print type of list1 <class:'tuple'>
    print(list1)

if __name__=='__main__':
    main()
