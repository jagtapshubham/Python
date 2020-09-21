#!/usr/bin/python3

def merge_list(list1,list2):
    list3=[]
    i=0
    j=0
    #Sorting list1 and list2
    list1.sort()
    list2.sort()
    
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    if i<len(list1):
        list3.extend(list1[i:])
    if j<len(list2):
        list3.extend(list2[j:])
    print("list1 and list2 after merge=",list3)

def main():
    list1,list2=[],[]
    
    #Accepting List 1
    l1_size=eval(input("Enter list 1 size="))
    for i in range(l1_size):
        num=eval(input("Enter list element="))
        list1.append(num)

    #Accepting list 2
    l2_size=eval(input("Enter list 2 size="))
    for i in range(l2_size):
        num=eval(input("Enter list 2 element="))
        list2.append(num)
    
    #Function call for merging two list
    merge_list(list1,list2)

#Call for main function
if __name__=='__main__':
    main()

