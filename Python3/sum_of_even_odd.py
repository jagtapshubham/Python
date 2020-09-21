#!/usr/bin/python3

lower_bound=eval(input("Enter lower bound"))
upper_bound=eval(input("Enter Upper bound"))

even_sum=0
odd_sum=0
for i in range(lower_bound,upper_bound):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("Even number sum in given range is%d"%even_sum)
print("Odd number sum in given range is %d"%odd_sum)
