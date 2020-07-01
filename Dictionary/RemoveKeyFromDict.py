#!/usr/bin/python3

def main():
    dict1={'1':"green",'2':"black",'3':"white",'4':"red"}
    print(dict1)
    key=input("Enter key to remove from dictionary=")
    if key in dict1:
        dict1.pop(key)
    print(dict1)

if __name__=='__main__':
    main()
