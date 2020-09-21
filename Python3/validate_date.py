#!/usr/bin/python

dd,mm,yy=eval(input("Enter date in dd,mm,yy="))

if dd>=1 and dd<=31:
	if mm>=1 and mm<=12:
		if yy>0:
			print("Date {}/{}/{} is valid".format(dd,mm,yy))	# .format is a method on string used to perform formating 
		else:
			print("yy=%d is invalid"%yy)
	else:
		print("mm=%d is invalid"%mm)
else:
	print("dd=%d is invalid",dd)

