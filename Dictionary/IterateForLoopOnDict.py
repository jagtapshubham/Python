#!/usr/bin/python3

def main():
    CodingLanguages={1:"C",2:"C++",3:"Java",4:"Python"}
    for dict_key,dict_value in CodingLanguages.item():
        print(dict_key,'->',dict_value)

if __name__=='__main__':
    main()
