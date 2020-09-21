#!/usr/bin/python3

def max_min(ls,size):
    max=ls[0]
    min=ls[0]
     
    for x in range(size):
        if ls[x]>max:
            max=ls[x]
        if ls[x]<min:
            min=ls[x]
    print("Maximum number is %d"%max)
    print("Minimum number is %d"%min)

def main():
    ls=[]
    size=eval(input("Enter size of list="))
    for i in range(size):
        num=eval(input("Enter elements="))
        ls.append(num)
    print(len(ls))
    max_min(ls,size)
        
if __name__=='__main__':
    main()
