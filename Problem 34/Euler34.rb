#!/usr/bin/env ruby

def fact(n)
	n < 1 ? 1 : n * fact(n - 1)
end

facts = []
totalsum = 0

for i in (0..9) do
	facts.push(fact(i))
end

for n in (10..100000) do
	digits = n.to_s.chars.map(&:to_i)
	sum = 0
	for d in digits do
		sum = sum + facts[d]
	end

	if sum == n then
		totalsum = totalsum + n
	end
end

puts totalsum