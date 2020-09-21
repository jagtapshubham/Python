#!/usr/bin/python3

def occurence_count(array):
    count=0
    print(array)
    key=eval(input("Enter key="))
    for i in array:
        if i==key:
            count+=1
    print(count)

def main():
    size=eval(input("Enter size of list="))
    array=[]
    i=0
    num=0
    for i in range(0,size):
        num=eval(input("Enter element="))
        array.append(num)
    occurence_count(array)

if __name__=='__main__':
    main()
