#!/usr/bin/python3

def list_intersection(list1,list2):
    intersection_list=[]
    i=0

    while i<len(list1):
        j=0
        while j<len(list2):
            if list1[i]==list2[j]:
                intersection_list.append(list1[i])
            j+=1
        i+=1
    print("Intersection element of two list are",intersection_list)
    
    
def main():
    list1=[]
    list2=[]
    i=0

    list1_size=eval(input("Enter list1 size="))
    for i in range(list1_size):
        num=eval(input("Enter list 1 element="))
        list1.append(num)
    list2_size=eval(input("Enter list2 size="))
    for i in range(list2_size):
        num=eval(input("Enter list 2 element="))
        list2.append(num)
    list_intersection(list1,list2)

if __name__=='__main__':
    main()
