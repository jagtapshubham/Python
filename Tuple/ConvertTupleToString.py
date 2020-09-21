#!/usr/bin/python3

def main():
    tuplex=('H','e','l','l','o','W','o','r','l','d')
    
    """
    The join() method provides a flexible way to create strings from iterable objects.
    It joins each element of an iterable (such as list, string and tuple).
    """
    str1="".join(tuplex)
    print(str1)

if __name__=='__main__':
    main()
