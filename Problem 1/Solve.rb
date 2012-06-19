#!/usr/bin/env ruby

# Project Euler problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.

solution = 0

for i in 1..999 do
	if (i % 3 == 0) || (i % 5 == 0) then
		solution += i
	end
	puts("Number " + i.to_s + ": solution = " + solution.to_s)
end

puts("Final solution = " + solution.to_s)