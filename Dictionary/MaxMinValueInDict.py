#!/usr/bin/python3

def MaxMin():
    dict1_values={'1':20,'2':15,'3':5,'4':17}
    key_max=max(dict1_values.values())
    key_min=min(dict1_values.values())
    print(key_max)
    print(key_min)

if __name__=='__main__':
    MaxMin()
