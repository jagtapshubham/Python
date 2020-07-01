#!/usr/bin/python3

def sort_keys():
    dict1={"black":1,"yellow":4,"white":2,"pink":3}
    for key in sorted(dict1):
        print("%s %s"%(key,dict1[key]))

if __name__=='__main__':
    sort_keys()
