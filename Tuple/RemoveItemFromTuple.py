#!/usr/bin/python3

def main():
    tuplex=(1,2,'e',4,5)
    print(tuplex)
    tuplex=list(tuplex)
    # Remember index number start from 0
    index=eval(input("Enter element index number to remove="))
    tuplex.pop(index)
    print(tuple(tuplex))


if __name__=='__main__':
    main()
