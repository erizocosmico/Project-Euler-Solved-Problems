#!/usr/bin/env python

# Project Euler exercise 2
# By considering the terms in the Fibonacci sequence whose values do 
# not exceed four million, find the sum of the even-valued terms.
# Tip: Fibonacci sequence is the sum of the two previous values
# Example: 1, 2, 3, 5, 8, 13, 21, 34, ...

a = 0
b = 1
fib = 1
sum = 0

while fib < 4000000:
  fib = a+b # Fibonacci term
  a, b = b, a+b # We assign the previous values to a and b
  if (fib % 2 == 0): # Is the fibonacci term even-valued?
	sum = sum + fib # Then add it to sum
	
print sum
# Prints 4613732