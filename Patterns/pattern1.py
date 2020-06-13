"""
*
* *
* * *
* * * *
"""

#!/usr/bin/python3

def main():
    x=0
    y=0
    num=eval(input("Enter number of rows="))
    for x in range(0,num):
        for y in range(0,x+1):
            print('*',end=" ")          #end=" " is used as \n in python3
        print(" ")

if __name__=='__main__':
    main()

