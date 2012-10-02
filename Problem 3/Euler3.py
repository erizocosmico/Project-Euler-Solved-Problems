#!/usr/bin/env python

# Project Euler exercise 3
# What is the largest prime factor of the number 600851475143?

from math import sqrt

n = 600851475143
factor = 2
largest_prime_factor = 0

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

# We're decomposing the number in prime factors
while n != 1:
  if (n % factor == 0 and is_prime(factor)):
	n = n/factor
	largest_prime_factor = factor
  else:
	factor = factor+1
	
print largest_prime_factor
# Prints 6857