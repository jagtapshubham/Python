#!/usr/bin/python3

def count_occurances(name1,search):
    index=0
    count=0
    while index!=-1:
        index=name1.find(search)
        if index!=-1:
            count+=1
            name1=name1[index+1:]
    return count

def main():
     name1=input("Enter String1=")
     search=input("Enter search string=")

     res=0
     res=count_occurances(name1,search)
     print(res)
     #print("%d occurances %d times in %d string"%search%res%name1)

if __name__=='__main__':
    main()
