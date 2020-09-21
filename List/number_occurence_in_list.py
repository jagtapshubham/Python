#!/usr/bin/python3

def main():
    i=0
    count=0
    l2=[1,2,3,4,5,6,7,5,8,5]
    key=eval(input("Enter element to count"))
    for x in l2:
        if key==x:
            count+=1                         # l2.count(key) is a build-in function to count   
    print(count)

if __name__=='__main__':
    main()
