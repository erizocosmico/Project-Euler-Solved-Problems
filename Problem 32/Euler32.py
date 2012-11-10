#!/usr/bin/env python
# -*- coding: utf-8 -*-

list = []
for i in xrange(1, 50):
    for j in xrange(1, 2000):
        if all(str(num) in "%d%d%d" % (i, j, i*j) for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]) and len(str("%d%d%d" % (i, j, i*j))) == 9 and not i*j in list:
            if len(str("%d%d%d" % (i, j, i*j))) > 9:
                break
            print "%d * %d = %d" % (i, j, i*j)
            list.append(i*j)
print sum(list)