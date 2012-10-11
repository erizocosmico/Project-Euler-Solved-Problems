#!/usr/bin/env python
# -*- coding: utf-8 -*-

def num_to_en_string(num):
    one_digit = {'0' : "", '1' : "one", '2' : "two", '3' : "three", '4' : "four", '5' : "five", '6' : "six", '7' : "seven", '8' : "eight", '9' : "nine"}
    two_digit = {'0' : "", '1' : "ten", '2' : "twenty", '3' : "thirty", '4' : "forty", '5' : "fifty", '6' : "sixty", '7' : "seventy", '8' : "eighty", '9' : "ninety"}
    teens = {'1' : "eleven", '2' : "twelve", '3' : "thirteen", '4' : "fourteen", '5' : "fifteen", '6' : "sixteen", '7' : "seventeen", '8' : "eighteen", '9' : "nineteen"}
    num = str(num)
    counter = len(num)
    result = []
    if counter == 1:
        result.append(one_digit[num[-1]])
    else:
        if counter == 2:
            if int(num) < 20 and int(num) > 10:
                result.append(teens[num[-1]])
            else:
                result.append(two_digit[num[-2]])
                result.append(one_digit[num[-1]])    
        else:
            if counter == 3:
                result.append(one_digit[num[-3]])
                if int(num[-2]) == 0 and int(num[-1]) == 0:
                    result.append("hundred")
                else:
                    result.append("hundredand")
                if int(num[-2:]) < 20 and int(num[-2:]) > 10:
                    result.append(teens[num[-1]])
                else:
                    result.append(two_digit[num[-2]])
                    result.append(one_digit[num[-1]])
            else:
                result.append("onethousand")
        counter -= 1
    print result
    return "".join(result)
    

def main():
    sum = 0
    for i in range(1, 1001):
        sum += len(num_to_en_string(i))
    print "If all the numbers from 1 to 1000 inclusive were written out in words would be used %d letters." % sum

if __name__ == "__main__":
    main()