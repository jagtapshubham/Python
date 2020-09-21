#!/usr/bin/python3

def add(a,b):
    return a+b
res=add(b=20,a=10)      #add(10,20) we can switch values using keyword argument
print(res)

#combination of keyword and default argument
#Note:-positional argument must be first & Once you start with keyword argument next argument after that must be keyword argument
res=add(10,10)
res=add(10,b=20)
res=add(b=10,a=10)
res=add(1,c=200,b=100)
