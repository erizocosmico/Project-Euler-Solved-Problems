#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_cycle_digits(num):
    cycle_len = 1
    while num % 2 == 0:
        num /= 2
    while num % 5 == 0:
        num /= 5
    while True:
        if (pow(10, cycle_len) - 1) % num == 0:
            return cycle_len
        else:
            cycle_len += 1
    
def main():
    d = 0
    d_digits = 0
    for i in xrange(2, 1000):
        digits = get_cycle_digits(i)
        if digits > d_digits:
            d_digits = digits
            d = i
    print d
    
if __name__ == "__main__":
    main()
        