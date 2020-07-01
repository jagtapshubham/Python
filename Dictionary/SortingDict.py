#!/usr/bin/python3

def main():
    dict1={1:'D',2:'B',3:'C',4:'A'}
    print("Ascending order")
    for x in sorted(dict1.values()):                    # dict1.values() is used to get values #dict.keys() is used to get key of dictionary
        print(x)
    print("Descending order")
    for x in sorted(dict1.values(),reverse=True):       #reverse=True is used for Decending sorting/Reverse order
        print(x)

if __name__=='__main__':
    main()
