#!/usr/bin/env python
# -*- coding: utf-8 -*-
        
def reduce(triangle):
    for i in xrange(1, len(triangle) + 1):
        for j in xrange(0, len(triangle) - i):
            triangle[len(triangle) - i - 1][j] += max(triangle[len(triangle) - i][j], triangle[len(triangle) - i][j + 1])
    return triangle[0][0]
    
def main():
    triangle = []
    with open('triangle.txt', 'r') as f:
        for line in f.readlines():
            triangle.append([int(i) for i in line.split()])
    print reduce(triangle)
    
if __name__ == "__main__":
    main()