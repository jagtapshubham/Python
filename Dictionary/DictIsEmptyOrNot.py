#!/usr/bin/python3

def IsEmptyorNot():
    dict1={}
    """    
    #Solution 1
    for i in dict1:
        print("Dictionary is Not Empty")
        break;
    else:
        print("Dictionary is Empty")
    """ 
    #Solution 2
    if not bool(dict1):         # As bool() method return Value TRUE or FALSE
        print("Empty")
    else:
        print("Not Empty")

if __name__=='__main__':
    IsEmptyorNot()
