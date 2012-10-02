#!/usr/bin/env python

# Project Euler exercise 6
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

squares_sum = 0
sum_squares = 0
numbers = range(1,101)

for i in numbers:
  squares_sum += i
  sum_squares += i**2

squares_sum = squares_sum**2

print squares_sum - sum_squares
# Prints 25164150