#!/usr/bin/env python3.9

from math import sqrt


class C:
    def __init__(self, pos):
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0
        self.side4 = 0
        self.pos = pos

    def __str__(self):
        return str(self.pos)


def rotate(xs):
    ys = list(xs)
    return tuple(ys[-1:] + ys[:-1])


count = 9
slen = sqrt(count)

cs = tuple(C(pos=n) for n in range(count))

for _ in range(count+1):
    for i in range(1, count+1):
        print(cs[i-1], end=" ")
        if i % slen == 0:
            print()
    cs = rotate(cs)
    print()
