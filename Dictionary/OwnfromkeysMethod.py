#!/usr/bin/python3

def from_keys(dict1,list1):
    if not isinstance(dict1,dict):              # isinstance() return TRUE is specified object is of specified type,else return FALSE
        return "dict1 is not a dictionary"
    index=0
    result={}
    list1_len=len(list1)
    key_len=len(dict1.keys())
    for i in dict1.keys():
        if index+1==key_len and index+1<list1_len:                #index+1 is taken because index is starting from 0 
            result[i]=list1[index:]
        elif index<list1_len:
            result[i]=list1[index]
            index+=1
        else:
            result[i]=None
    return result


def main():
    dict1={'name':'Shubham','age':24,'marks':50,}
    list1=[5,6,7,8]
    result=from_keys(dict1,list1)
    print(result)

if __name__=='__main__':
    main()
