#!/bin/python3

import sys

def pythagoreanTriple(a):
    # a = (m^2 - n^2)
    
    if a%2 == 0:
        # a = 2mn
        m, n = a//2, 1
        return [a, m**2-n**2, m**2+n**2]
    else:
        # a = (m-n)(m+n)
        m = (a+1)//2
        n = (a-1)//2
        return [a, 2*m*n, m**2+n**2]

a = int(input().strip())
triple = pythagoreanTriple(a)
print (" ".join(map(str, triple)))
