package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(n string) bool {
	x := len(n) / 2
	s1 := n[:x]
	s2 := n[len(n) - x:]
	for i := 0; i < x; i++ {
		if s1[i] != s2[x - 1 - i] {
			return false
		}
	}
	return true
}

func main() {
	var sum, i int64 = 0, 1
	for ; i < 1000000; i++ {
		if isPalindrome(strconv.FormatInt(i, 10)) && isPalindrome(strconv.FormatInt(i, 2)) {
			sum += i
		}
	}

	fmt.Printf("The sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is %d.", sum)
}