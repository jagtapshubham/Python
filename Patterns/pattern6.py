"""
* * * * * * *  
  * * * * *  
    * * *  
      *  
"""

#!/usr/bin/python3

def main():
    row=eval(input("Enter number of rows="))
    odd=row*2-1
    for i in range(0,row):
        for k in range(0,i):
            print(" ",end=" ")
        for j in range(0,odd):
            print("*",end=" ")
        odd-=2
        print(" ")

if __name__=='__main__':
    main()
