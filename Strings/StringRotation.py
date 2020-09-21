#!/usr/bin/python3

def SingleCharRotation(input_str,sub_str):
    cp_inputstr=input_str
    i=0
    while i<len(input_str):
        input_str=input_str[-1]+input_str[:-1]
        if input_str in sub_str:
            print("{} is rotation of {}".format(sub_str,cp_inputstr))
            return
        i+=1
    print("{} is not rotation of {}".format(sub_str,cp_inputstr))

def main():
    input_str=input("Enter String=")
    sub_str=input("Enter String to find in string=")
    SingleCharRotation(input_str,sub_str)

if __name__=='__main__':
    main()
