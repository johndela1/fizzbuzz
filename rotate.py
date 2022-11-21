#!/usr/bin/env python3.9

from math import isqrt


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
    return tuple(xs[-1:] + xs[:-1])


count = 4
slen = isqrt(count)

# possibly remove constraint and fill to next highest square
assert count == slen ** 2, "count must be square number"

cs = tuple(C(pos=n) for n in range(count))

for _ in range(count+1):
    for i in range(1, count+1):
        print(cs[i-1], end=" ")
        if i % slen == 0:
            print()
    cs = rotate(cs)
    print()
