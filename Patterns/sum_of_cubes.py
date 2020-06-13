#!/usr/bin/python3

def main():
    sum=0
    rem=0
    num=eval(input("Enter the number="))
    while(num!=0):
        rem=num%10
        num=int(num/10)
        sum=rem*rem*rem+sum
    print("Sum of cube of digit=%d"%sum)

if __name__=='__main__':
    main()
