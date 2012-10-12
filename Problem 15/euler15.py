#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import factorial

# C = n! / r!*(n-r)!

if __name__ == "__main__":
	(n, r) = (40, 20)
	print factorial(n) / (factorial(r) * factorial(n - r))