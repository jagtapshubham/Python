#!/usr/bin/python3

num=eval(input("Enter number"))
sum=0
while num!=0:
    sum+=num
    num=eval(input("Enter number again"))
print(sum)
