#!/usr/bin/python3

def main():
    tuplex=(1,2,1,3,4,2)
    print(tuplex)
    dict1={}
    for i in tuplex:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    print(dict1)

if __name__=='__main__':
    main()
