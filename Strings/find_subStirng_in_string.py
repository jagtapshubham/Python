#!/usr/bin/python3

def substring_in_string(text,search):
    index=0
    count=0
    while index!=-1:                # find() function returns -1 in failure so -1 is used
        index=text.find(search)
        if index!=-1:
            count+=1
            text=text[index+1:]     # this line is used to avoid counting always from starting
    return count


def main():
    text=input("Enter String=")
    substring=input("Enter Substring to search in string=")
    occurrence=0
    occurrence=substring_in_string(text,substring)
    print(occurrence)

if __name__=='__main__':
    main()
