#!/usr/bin/env python

# Project Euler exercise 4
# Find the largest palindrome made from the product of two 3-digit numbers.
# Tip: A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.

a = 999
b = 999
l = []
pal = 0

def int_to_list(i):
  s = str(i)
  l = []
  for c in s:
    l.append(c)
  return l

def is_palindrome(l):
  n = len(l)/2
  if (len(l) % 2 == 0):
    max = n
    get = n
  else:
	max = n-1
	get = n+1
  first_part = l[0:n]
  second_part = l[get:]
  first_part.reverse()
  is_palindrome = True
  for i in range(0, max):
    if (first_part[i] != second_part[i]):
	  is_palindrome = False
	  break
  return is_palindrome

while a > 900:
  while b > 900:
	n = a*b
	l = int_to_list(n)
	if is_palindrome(l):
	  if pal < n:
	    pal = n
	b = b-1
  b = 999
  a = a-1

print pal
# Prints 906609