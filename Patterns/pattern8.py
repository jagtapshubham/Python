"""
A  
A B  
A B C  
A B C D 
"""

#!/usr/bin/python3

def main():
    rows=eval(input("Enter Number of rows="))
    for i in range(1,rows+1):
        for j in range(65,65+i):
            print("%c"%j,end=" ")
        print(" ")

if __name__=='__main__':
    main()
