#!/usr/bin/python3

def main():
    tup=((1,'s'),(2,'j'))
    dict1={}
    for x,y in tup:
        dict1[y]=x
    print(dict1)

if __name__=='__main__':
    main()
