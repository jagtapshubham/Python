#!/usr/bin/python3

n=eval(input("Enter n="))
i=0
sum=0
while i<n:
    num=eval(input("Enter number="))
    if num%2==0:
        print("%d is even number"%num)
        sum=sum+num
    i+=1 
print("Sum %d of even number"%sum)
