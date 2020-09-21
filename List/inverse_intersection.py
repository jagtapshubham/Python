#!/usr/bin/python3

def inverse_intersection(list1,list2,ct):
    inverse_list=[]
    i=0

    while i<len(list1):
        count=0
        j=0
        while j<len(list2):
            if list1[i]==list2[j]:
                count+=1
                break
            j+=1
        if count==0:
            inverse_list.append(list1[i])
        i+=1
    print(inverse_list)
    if ct==0:
        li=inverse_intersection(list2,list1,1)

def main():
    list1=[]
    list2=[]

    #Accepting list 1 element
    list1_size=eval(input("Enter size of list1="))
    for i in range(list1_size):
        num=eval(input("Enter list1 element="))
        list1.append(num)

    # Accepting list 2 element
    list2_size=eval(input("Enter size of list2="))
    for i in range(list2_size):
        num=eval(input("Enter list2 element="))
        list2.append(num)
    
    # inverse_intersection function call
    inverse_intersection(list1,list2,0)

if __name__=='__main__':
   main() 
