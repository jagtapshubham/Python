#!/usr/bin/python3

def variableArgsAdd(*args):
    sum=0
    print(type(args))
    for i in args:
        sum+=i
    return sum

res=variableArgsAdd(10,20,30,40,50)
print(res)
