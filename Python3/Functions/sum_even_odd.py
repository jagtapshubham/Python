#!/usr/bin/python3

print("Its fun")
lb=eval(input("Enter lower bound"))
ub=eval(input("Enter upper bound"))

def sumevenodd(lb,ub):
    sumeven=0
    sumodd=0
    while lb<ub:
        if lb%2==0:
            sumeven += lb
        else:
            sumodd += lb
        lb+=1
    return sumeven,sumodd

if __name__=='__main__':
    reseven,resodd=sumevenodd(lb,ub)
    print("Even Sum %d"%reseven)
    print("Odd Sum %d"%resodd)
