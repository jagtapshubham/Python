"""
      A  
    B A B  
  C B A B A  
D C B A B A B 
"""

#!/usr/bin/python3

def main():
    odd=1
    rows=eval(input("Enter number of rows="))
    for i in range(0,rows):
        alpha=65
        for k in range(1,rows-i):
            print(" ",end=" ")
        alpha+=i
        for j in range(0,odd):
            if alpha==65:
                print("%c"%alpha,end=" ")
                alpha+=1
            else:
                print("%c"%alpha,end=" ")
                alpha-=1
        odd+=2
        print(" ")

if __name__=='__main__':
    main()
