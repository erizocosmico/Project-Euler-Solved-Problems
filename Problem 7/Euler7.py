#!/usr/bin/env python

# Project Euler exercise 7

from math import sqrt

count = 22
number = 74

# We wanna know if a number is prime or not
# A number n is prime if n is not divisible by any number between 2 and its square root
def is_prime(n):
  max = sqrt(n)
  i = 2
  is_prime = True
  while i < max:
	if (n % i == 0):
	  is_prime = False
	else:
	  i = i+1
  return is_prime

while count <= 2001:
  if number%2 != 0:
    if number%3 != 0:
      if number%5 != 0:
        if is_prime(number):
          print number, count
          count += 1
  number += 1

print number
  