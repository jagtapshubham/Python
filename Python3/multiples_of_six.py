#!/usr/bin/python3

low=eval(input("Enter starting range="))
upper=eval(input("Enter ending range="))

for i in range(low,upper):
    if i%6==0:
        print(i)

