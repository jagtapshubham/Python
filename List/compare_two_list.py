#!/usr/bin/python3

def sort_fun(li): 
    i=0
    while i<len(li):
        temp=0
        j=0
        while j<(len(li)-1):
            if li[j]>li[j+1]:
                temp=li[j]
                li[j]=li[j+1]
                li[j+1]=temp
            j+=1
        i+=1
    return li

def compare_list(l1,l2):
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if l1[i] == l2[j]:
            i+=1
            j+=1
            continue
        else:
            return 1

def main():
    l1=[]
    l2=[]
    res=0

    l1_size=eval(input("Enter size of l1 list="))
    for i in range(l1_size):
        num=eval(input("Enter l1 element="))
        l1.append(num)
    l2_size=eval(input("Enter size of l2 list="))
    for i in range(l2_size):
        num=eval(input("Enter l2 element="))
        l2.append(num)
    if l1_size==l2_size:
        sort_fun(l1)
        sort_fun(l2)
        res=compare_list(l1,l2)
        if res==1:
            print("List are not same")
        else:
            print("List are same")
    else:
        print("List1 is not equal to list2 in length")

if __name__=='__main__':
    main()
