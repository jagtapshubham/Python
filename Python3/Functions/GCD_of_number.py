#!/usr/bin/python3

def gcd_of_number(no1,no2):
    if no1==no2:
        return 0
    else:
        while no1!=no2:
            if no1>no2:
                no1-=no2
            else:
                no2-=no1
        return no1

def main():
    no1,no2=eval(input("Enter Two number +ve Num1,Num2="))
    gcd=gcd_of_number(no1,no2)
    print("GCD of %d and %d is %d"%(no1,no2,gcd))
    #print(gcd)

if __name__=='__main__':
    main()

