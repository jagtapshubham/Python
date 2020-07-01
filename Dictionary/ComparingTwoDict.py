#!/usr/bin/python3

def Comparing_Dictionary(dict1,dict2):
    retval=True
    if type(dict1)!=dict or type(dict2)!=dict:
        return False

    for key in dict1:
        if key in dict2 and dict1[key]==dict2[key]:
            continue
        retval=False
        break
    return retval

def main():
    dict1={1:2,2:3}
    dict2={1:3,2:2}
    result=False
    if(len(dict1)==len(dict2)):
        result=Comparing_Dictionary(dict1,dict2)
    if result==True:
        print("Dictionary are same")
    else:
        print("Dictionary are not same")

if __name__=='__main__':
    main()
