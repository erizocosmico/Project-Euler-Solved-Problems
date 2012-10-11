#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("numbers.txt", 'r') as f:
        sum = 0
        for n in f.readlines():
            sum += int(n.replace('\n', ''))
    print str(sum)[0:10]
    # 5537376230
    
if __name__ == "__main__":
    main()
