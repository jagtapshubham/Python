#!/usr/bin/python

hrs,min,sec=eval(input("Enter in following format hrs,min,sec="))

if hrs>=0 and hrs<24:
    if min>=0 and min<60:
        if sec>=0 and sec<60:
            print("{}.{}.{} is valid time".format(hrs,min,sec))
        else:
            print("sec is invalid")
    else:
        print("Minutes are invalid")
else:
    print("Hours are invalid")
