#!/usr/bin/python3

def main():
    set1=set([10,5,20,40,30])
    max=min=list(set1)[0]
    for i in set1:
        if i>max:
            max=i
        if i<min:
            min=i
    print("Max=%d"%max)
    print("Min=%d"%min)

if __name__=='__main__':
    main()
