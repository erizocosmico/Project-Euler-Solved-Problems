#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    m = [[0 for i in xrange(0, 8)] for j in xrange(0, 201)]
    for t in xrange(0, 201):
        for i in xrange(0, len(coins)):
            if t >= coins[i]:
                m[t][i] += m[t - coins[i]][i]
            if i == 0:
                m[t][i] = 1
            else:
                m[t][i] += m[t][i - 1]
    print m[200][7]