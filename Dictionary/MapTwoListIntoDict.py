#!/usr/bin/python3

def main():
    key=['1','2','3','4']
    values=["green","yellow","orange","blue"]

    """
    #Solution 1
    dict1={}
    j=0
    for i in key:
        dict1[i]=values[j]
        j+=1
    print(dict1)
    """
    #Solution 2
    color_dictionary=dict(zip(key,values))  #zip() is used to bind two objects together   
    print(color_dictionary)

if __name__=='__main__':
    main()
