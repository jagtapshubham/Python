#!/usr/bin/python3

def main():
    dict1={"car":"Ford","model":"Sports","chasino":1234}
    key=input("Enter key to find=")
    if key in dict1:
        print("{} key found with value {}".format(key,dict1.get(key)))

if __name__=='__main__':
    main()
