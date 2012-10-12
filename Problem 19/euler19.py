#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    return False

def main():
    sundays = 0
    current_week_day = 2
    months = {"1" : 31,  "2" : 28, "3" : 31, "4" : 30, "5" : 31, "6" : 30, "7" : 31, "8" : 31, "9" : 30, "10" : 31, "11" : 30, "12" : 31}
    for year in xrange(1901, 2001):
        if is_leap(year):
            months['2'] = 29
        else:
            months['2'] = 28
        for month in xrange(1, 13):
            for day in xrange(1, months[str(month)] + 1):
                if day == 1 and current_week_day == 7:
                    sundays += 1
                current_week_day += 1
                if current_week_day > 7:
                    current_week_day = 1
    print "%d Sundays fell on the first of the month during the twentieth century." % sundays
    
if __name__ == "__main__":
    main()