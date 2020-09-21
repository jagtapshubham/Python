#!/usr/bin/python3

no1,no2,no3=eval(input("Enter three numbers="))

if no1>no2 and no1>no3:
        print("%d number is greater"%no1)
elif no2>no3:
    print("%d number is greater"%no2)
else:
    print("%d number is greater"%no3)
