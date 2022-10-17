from collections import Counter as ct # se usa contador

def solution(s):
    c = ct(s)
    for i in s: 
       if c[i] == 1 :
        return i
        
    return "_"
    