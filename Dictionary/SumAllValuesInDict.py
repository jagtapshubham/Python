# Problem: Sum all the Dictionary values

#!/usr/bin/python3

def main():
    dict1={1:100,2:300,3:50}
    
    #Solution 1

    dictsum=0
    for x,y in dict1.items():
        dictsum=dictsum+y
    print(dictsum)

    #Solution 2

    print(sum(dict1.values()))

if __name__=='__main__':
    main()
