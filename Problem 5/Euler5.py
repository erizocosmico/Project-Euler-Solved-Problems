#!/usr/bin/env python

# Project Euler Exercise 5
# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

def is_divisible(n):
  i = 2
  is_divisible = True
  while i <= 20:
	if (n%i != 0):
	  is_divisible = False
	  break
	i = i+1
  return is_divisible

i = 20
while True:
  if is_divisible(i):
	print i # Prints 232792560
	break
  else:
	i = i+20
	