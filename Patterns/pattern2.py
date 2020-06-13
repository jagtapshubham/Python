"""
* * * *
* * *
* *
*
"""

#!/usr/bin/pattern3

def main():
    row=eval(input("Enter number of rows="))
    for i in range(0,row):
        for j in range(0,row-i):
            print("*",end=" ")
        print(" ")

if __name__=='__main__':
    main()
