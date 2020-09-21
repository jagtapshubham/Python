#!/usr/bin/python3

def add(a,b=10):
    return a+b
res=add(100,200)    #b=200 is overwrite b=10
print(res)
ref=add(100)        #b=10 is taken as default value
print(ref)
