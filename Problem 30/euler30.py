#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_digits_power(num):
    s = 0
    for n in str(num):
        s += int(n) ** 5
    return True if s == num else False

if __name__ == "__main__":
    print sum([i for i in xrange(2, 198000) if get_digits_power(i)])