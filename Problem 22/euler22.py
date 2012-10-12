#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_name_chars_score(name, chars):
    score = 0
    for char in name:
        score += chars[char]
    return score

def main():
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chars = {}
    i = 1
    for char in abc:
        chars[char] = i
        i += 1
    with open('names.txt', 'r') as f:
        for line in f.readlines():
            names = [name.replace('"', '') for name in line.split(",")]
    names.sort()
    sum = 0
    i = 1
    for name in names:
        sum += get_name_chars_score(name, chars) * i
        i += 1
    print sum    
    
if __name__ == "__main__":
    main()