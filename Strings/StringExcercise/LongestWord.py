#!/usr/bin/python3

def main(word_list):
    word_len=[]
    for n in word_list:
        word_len.append((len(n),n))
    word_len.sort()
    print(word_len)
  
if __name__=='__main__':
    main(["PHP","Exercise","Hello"])
