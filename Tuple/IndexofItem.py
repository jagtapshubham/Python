#!/usr/bin/python3

def main():
    tuplex=(1,2,3,4,4,"p",7)
    print(tuplex)
    #Enter element 
    index=tuplex.index("p")
    print("p at index=%d"%index)
    # Enter element with starting index number from to search
    index=tuplex.index(3,1)
    print("3 at index %d"%index)
    # Enter element with starting and ending index to search
    index=tuplex.index(4,2,6)
    print("4 at index %d"%index)

if __name__=='__main__':
    main()
