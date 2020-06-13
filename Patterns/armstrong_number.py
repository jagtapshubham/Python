#!/usr/bin/python3

def armstrong_number(num):
    res=num
    sum=0
    rem=0
    while num!=0:
        rem=num%10
        num=int(num/10)
        sum=rem*rem*rem+sum
    if sum==res:
        print("Number is armstrong")
    else:
        print("Number is nnot armstrong")

def main():
	num=eval(input("Enter number="))
	armstrong_number(num)

if __name__=='__main__':
    main()
