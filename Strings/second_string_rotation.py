#!/usr/bin/python3

def second_string_rotation(input_str,rotation_str):

    if len(input_str)!=len(rotation_str):
        return False
    return rotation_str in input_str+input_str

if __name__=='__main__':
    input_str=input("Enter string=")
    rotation_str=input("Enter rigth string rotation of string=")
    if second_string_rotation(input_str,rotation_str):
        print("{} is rotation of {}".format(rotation_str,input_str))
    else:
        print("{} is not rotation of {}".format(rotation_str,input_str))
    
