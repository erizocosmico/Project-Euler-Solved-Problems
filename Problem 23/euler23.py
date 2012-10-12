#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_divisors(num):
    return [i for i in xrange(1, num) if num % i == 0]

def main():
    abundants = {}
    sum_ = 0
    for i in xrange(12, 28123):
        print "Search for %d" % i
        if sum(get_divisors(i)) > i:
            abundants[i] = i
            print "%d is abundant" % i

    for i in xrange(1, 28123):
        print "Searching if %d can be written as the sum of two abundant numbers" % i
        for j in abundants:
            try:
                is_sum = True
                x = abundants[i - j]
                break
            except:
                is_sum = False
        if not is_sum:
            sum_ += i
    print "The sum of all the positive integers which cannot be written as the sum of two abundant numbers is %d" % sum_
    
if __name__ == "__main__":
    main()