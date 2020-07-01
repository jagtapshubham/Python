#!/usr/bin/python3

def RemoveDuplicate():
    dict1={"orange":1,"blue":3,"red":4,"green":2,"red":5}
    result={}
    for key,value in dict1.items():
        if key not in result.keys():
            result[key]=value
    print(result)

if __name__=='__main__':
    RemoveDuplicate()
