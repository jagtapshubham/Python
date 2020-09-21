#!/usr/bin/python3

def insert():
    l2=[1,2,3,4,5]
    print(l2)
    l2.insert(2,10)
    print(l2)

def pop():
    l2=[1,2,3,4,5]
    print(l2)
    l2.pop()        #pops th last index element
    l2.pop(1)       #pops the 1 index element
    print(l2)

def main():
    insert()
    pop()

if __name__=='__main__':
    main()
