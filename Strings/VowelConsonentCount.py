#!/usr/bin/python3

def vowel_consonent_count(string):
    cvowel=0
    cconsonent=0
    cdigit=0
    cspchar=0
    for i in string:
        if i>='a' and i<='z' or i>='A' and i<='Z':
            i=i.lower()
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                cvowel+=1
            else:
                cconsonent+=1
        elif i>='0' and i<='9':
            cdigit+=1
        else:
            cspchar+=1
    print("Vowel count in string=%d"%cvowel)
    print("Consonent count in string=%d"%cconsonent)
    print("Digits count in string=%d"%cdigit)
    print("Special character count in string=%d"%cspchar)


def main():
    string=input("Enter String=")
    vowel_consonent_count(string)

if __name__=='__main__':
    main()
