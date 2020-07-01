#!/usr/bin/python3

def main():
    dict1={'a':100,'b':200}
    dict2={'a':300,'y':400}     # Keys should not be same otherwise it will update existing key instead of merging
    dict1.update(dict2)
    print(dict1)

if __name__=='__main__':
    main()
