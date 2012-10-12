#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

def is_prime(num):
    if num < 0:
        num = -num
    if not num in [0, 1]:
        if num % 2 != 0 and num % 3 != 0 and num % 4 != 0 and num % 5 != 0 or num in [2, 3, 4, 5]:
            i = 7
            while i < floor(sqrt(num)) + 1:
                if num % i == 0:
                    return False
                    break
                i += 1
            return True
    return False
    
def main():
    (m, ma, mb) = (0, 0, 0)
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
            if n + 1 > m:
                (m, ma, mb) = (n, a, b)
    print ma * mb
                    
if __name__ == "__main__":
    main()