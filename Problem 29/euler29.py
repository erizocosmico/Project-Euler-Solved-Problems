#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set

if __name__ == "__main__":
    numbers = [a ** b for a in xrange(2, 101) for b in xrange(2, 101)]
    print len(Set(numbers))
            
            