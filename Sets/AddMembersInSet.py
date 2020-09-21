#!/usr/bin/python3

def main():
    s=set(["Red"])
    x=input("Enter color=")
    s.add(x)
    s.update(['green','yellow'])
    print(s)

if __name__=='__main__':
    main()
