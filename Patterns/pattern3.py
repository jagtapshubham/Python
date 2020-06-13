"""
      *
    * *
  * * *
* * * *
"""

#!/usr/bin/python3

def main():
    rows=eval(input("Enter number of rows="))
    for i in range(1,rows+1):
        for k in range(0,rows-i):
            print(" ",end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print(" ")

if __name__=='__main__':
    main()
