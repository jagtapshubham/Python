#!/usr/bin/python3
from copy import deepcopy

def main():
    tuplex=('hello',5,[],True)
    print(tuplex)
    #make a deepcopy using deepcopy() function
    tuplex_colon=deepcopy(tuplex)
    tuplex_colon[2].append(50)
    print(tuplex_colon)
    print(tuplex)

if __name__=='__main__':
    main()
