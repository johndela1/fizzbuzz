#!/usr/bin/env python3.9


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]


def perm(seq, i, n):
    if i >= n:
        print(seq)
    else:
        for j in range(i, n):
            swap(seq, j, i)
            perm(seq, i + 1, n)
            swap(seq, j, i)


l = [0, 1]
swap(l, 0, 1)
assert l == [1, 0]
swap(l, 0, 1)
assert l == [0, 1]

seq = [*'012']
perm(seq, 0, len(seq))
