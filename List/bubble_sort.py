#!/usr/bin/python3

def sort_fun(l1):
    i=0
    while i<len(l1):
        j=0
        temp=0
        while j<(len(l1)-1):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
            j+=1
        i+=1
    return l1

def main():
    l1=[]
    size=eval(input("Enter size of list="))
    for i in range(size):
        num=eval(input("Enter element="))
        l1.append(num)
    sort_fun(l1)
    print(l1)

if __name__=='__main__':
    main()
