#!/usr/bin/python3

def char_count(string):
    result={}
    for i in string:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    return result

def main():
    string=input("Enter String=")
    res=char_count(string)
    print(res.sorted())

if __name__=='__main__':
    main()
