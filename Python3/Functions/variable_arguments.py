#!/usr/bin/python3

def variableArgAdd(*args):
    print(type(args))
    for x in args:
        print(x)
variableArgAdd(1,2,3)
variableArgAdd(1,2,3,4,5,6,7,8)
