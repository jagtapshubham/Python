#!/usr/bin/python3

def main():
    dict1={1:10,2:20}
    dict2={3:30,4:40}
    dict3={5:50,6:60}
    dict4={}
    for d in (dict1,dict2,dict3):
        print(d)
        dict4.update(d)
    print(dict4)

if __name__=='__main__':
    main()
