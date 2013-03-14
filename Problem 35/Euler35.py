#!/usr/bin/env python

def rotations(n):
	rotations = []
	rotations.append(n)
	n = str(n)
	for i in xrange(1, len(n)):
		n = n[1:] + n[0]
		rotations.append(int(n))
	return rotations

def is_prime(n):
	if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n <= 1:
		return False
	else:
		for i in range(3, int(n ** 0.5) + 1, 2):
			if n % i == 0:
				return False
	return True

def is_circular_prime(n):
	is_circular = True
	for i in rotations(n):
		if not is_prime(i):
			is_circular = False
			break
	return is_circular

circular_primes = [i for i in xrange(100, 1000000) if is_circular_prime(i)]

print "There are %d circular primes below 1M." % (len(circular_primes) + 13)