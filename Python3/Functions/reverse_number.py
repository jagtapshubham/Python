#!/usr/bin/python3

def reverse_number(num):
    rem=0
    rev=0
    while num!=0:
        rem=num%10
        num=int(num//10)     #  floor division is used and type casting is done to interger
        rev=rev*10+rem
    return rev

def pallindrome(num):
    rev=0
    rem=0
    number=num
    while num!=0:
        rem=num%10
        num=int(num//10)     #  floor division is used and type casting is done to interger
        rev=rev*10+rem
    if number==rev:
        print("Number is pallindrome")
    else:
        print("Number is not pallindrome")

def main():
    num=eval(input("Enter number="))
    reverse=reverse_number(num)
    print(reverse)
    pallindrome(num)

if __name__=='__main__':
    main()
