#!/usr/bin/python3

def main():
    dict1={"one":25,"two":2,"three":20,"four":5}

"""
    #Solution 1
    multi_value=1
    for x,y in dict1.items():
        multi_value=multi_value*y
    print(multi_value)
"""

    #Solution 2
    multi_value=1
    for x in dict1:
        multi_value*=dict1[x]
    print(multi_value)

if __name__=='__main__':
    main()
