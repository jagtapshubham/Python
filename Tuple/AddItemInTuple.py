#!/usr/bin/python3

def main():
    tuplex=(1,2,3)
    print(tuplex)
    
    #tuples are immutable,so you cannot add new elements
    #using merge of tuple with + operator you can add element and it will create a new tuple
    tuplex=tuplex+(4,)
    print(tuplex)
    
    #add element at paricular index in tuple
    tuplex=tuplex[:4]+(5,6,7)
    print(tuplex)

if __name__=='__main__':
    main()
