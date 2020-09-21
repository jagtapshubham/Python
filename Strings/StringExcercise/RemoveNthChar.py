"""Output
pyton
"""

#!/usr/bin/python3

def remove_nth_char(string,n):
    first_part=string[:n]
    last_part=string[n+1:]
    return first_part+last_part

if __name__=='__main__':
    print(remove_nth_char("Python",3))
