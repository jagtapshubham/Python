#!/usr/bin/python3

def union_of_list(list1,list2):
    union_list=[]
    i=0
    union_list.extend(list1)        # copy list 1 to union_list to avoid rechecking of duplicate element loop

    while i<len(list2):             # increase i till length of list 2
        count=0
        j=0
        while j<len(list1):             # increase j till length of list 1 
            if list2[i]==union_list[j]: # if element of list2 found in union_list then break,because it is already present in union_list
                count+=1                    
                break
            j+=1
        if count==0:                    #if count is zero then element of list two is not present in union_list,add the list2 element in list
            union_list.append(list2[i])
        i+=1
    union_list.sort()
    print(union_list)

def main():
    list1=[]
    list2=[]
    i=0

    list1_size=eval(input("Enter list1 size="))
    for i in range(list1_size):
        num=eval(input("Enter list1 element="))
        list1.append(num)
    list2_size=eval(input("Enter list2 size="))
    for i in range(list2_size):
        num=eval(input("Enter list2 element="))
        list2.append(num)
    union_of_list(list1,list2)

if __name__=='__main__':
    main()

