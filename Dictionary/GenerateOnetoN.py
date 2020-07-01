#!/usr/bin/python3

def main():
    dict_square={}
    n=eval(input("Enter n="))
    x=1
    while(x<=n):
        dict_square[x]=int(x*x)
        x+=1
    print(dict_square)

if __name__=='__main__':
    main()
