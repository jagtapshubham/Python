"""
      *  
    * * *  
  * * * * *  
* * * * * * *  
  * * * * *  
    * * *  
      *  
"""

#!/usr/bin/python3

def main():
    odd=-1
    row=eval(input("Enter number of row="))
    for i in range(1,row*2):
        if i<=row:
            odd+=2
            for k in range(0,row-i):
                print(" ",end=" ")
            for j in range(0,odd):
                print("*",end=" ")
        else:
            odd-=2
            for k in range(0,i-row):
                print(" ",end=" ")
            for j in range(0,odd):
                print("*",end=" ")
        print(" ")

if __name__=='__main__':
    main()
