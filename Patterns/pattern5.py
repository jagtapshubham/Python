"""
      *  
    * * *  
  * * * * *  
* * * * * * *
"""

#!/usr/bin/python3

def main():
    odd=1
    row=eval(input("Enter number of rows="))
    for i in range(1,row+1):
        for k in range(0,row-i):
            print(" ",end=" ")
        for j in range(0,odd):
            print("*",end=" ")
        odd+=2
        print(" ")

if __name__=='__main__':
    main()
