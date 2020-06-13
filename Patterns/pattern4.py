"""
* * * *
  * * *
    * *
      *
"""

#!/usr/bin/python3

def main():
    row=eval(input("Enter Number of rows="))
    for i in range(0,row):
        for k in range(0,i):
            print(" ",end=" ")
        for j in range(0,row-i):
            print("*",end=" ")
        print(" ")

if __name__=='__main__':
    main()
