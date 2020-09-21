#!/usr/bin/python3

x=1
while x!=7:         # x!=0 condition doesnt execute else
    if x%7==0:
        break
    print(x)
    x+=1
else:
    print("Else of while")
