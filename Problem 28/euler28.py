#!/usr/bin/env python
# -*- coding: utf-8 -*-

def draw_spiral(num):
    spiral = [[i for i in xrange(0, num)] for j in xrange(0, num)]
    (xpos, ypos) = (num / 2, num / 2)
    (x, y, num_, dir, xmov, ymov, mov, movs, moved) = (0, 0, 1, 0, 0, 0, 0, 0, 0)
    while num_ <= num ** 2:
        spiral[ypos + y][xpos + x] = num_
        if dir == 0:
            xmov += 1
            x = xmov
            mov += 1
            if moved == 0:
                movs += 1
                moved = 1
            if mov == movs:
                (moved, mov, dir) = (0, 0, 1)
            else:
                dir = 0
        elif dir == 1:
            ymov += 1
            y = ymov
            mov += 1
            if mov == movs:
                (mov, dir) = (0, 2)
        elif dir == 2:
            xmov -= 1
            x = xmov
            mov += 1
            if moved == 0:
                movs += 1
                moved = 1
            if mov == movs:
                (mov, dir, moved) = (0, 3, 0)
        else:
            ymov -= 1
            y = ymov
            mov += 1
            if mov == movs:
                (dir, moved, mov) = (0, 0, 0)
        num_ += 1
    return spiral  

if __name__ == "__main__":
    num_spiral = 1001
    spiral = draw_spiral(num_spiral)
    diag_sum = 0
    for i in xrange(0, num_spiral):
        diag_sum += spiral[i][i]
        diag_sum += spiral[i][num_spiral - 1 - i]
    diag_sum -= 1
    print diag_sum
    # Prints 669171001