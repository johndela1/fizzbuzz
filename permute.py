#!/usr/bin/env python3.9

import itertools


def ref_perms(syms):
    return [
        "".join(str(p) for p in ps)
        for ps in itertools.permutations(list(syms))
    ]


def count(to, syms):
    def inc(n):
        lsd = n[-1]
        rest = n[0:-1]
        if rest == "":
            rest = syms[0]
        if lsd == syms[-1]:
            return inc(rest) + syms[0]
        else:
            if rest == syms[0]:
                rest = ""
            return rest + syms[syms.index(lsd) + 1]

    n = syms[0]
    for _ in range(to):
        yield n.zfill(len(syms))
        n = inc(n)


def all_but(seq, i):
    return seq[:i] + seq[i + 1 :]


def flatten(l):
    flat = []
    for i in l:
        if type(i) == int:
            flat.append(i)
            continue
        for j in i:
            flat.append(j)

    return flat


def perms(xs):
    if len(xs) == 0:
        return [[]]
    if len(xs) == 1:
        return [xs]
    ps = []
    for i, x in enumerate(xs):
        ps.append(flatten([x] + perms(all_but(xs, i))))
    return [ps]


def count_perms(syms):
    return [
        n
        for n in count(len(syms) ** len(syms), syms)
        if len(n) == len(syms) and len(set(n)) == len(n)
    ]


syms = []
print("exp", ref_perms(syms))
print("got", perms(syms))

syms = [0]
print("exp", ref_perms(syms))
print("got", perms(syms))

syms = [0, 1]
print("exp", ref_perms(syms))
print("got", perms(syms))


def fix(ps):
    return flatten([(flatten([xs[0], ys])) for ys in xs[1:]] for xs in ps[0])


def all_but(seq, i):
    return seq[:i] + seq[i + 1 :]


def flatten(l):
    flat = []
    for i in l:
        if type(i) == int:
            flat.append(i)
            continue
        for j in i:
            flat.append(j)

    return flat


def perms(xs):
    if len(xs) == 0:
        return [[]]
    if len(xs) == 1:
        return [xs]
    ps = []
    for i, x in enumerate(xs):
        ps.append(flatten([x] + perms(all_but(xs, i))))
    return [ps]


syms = []
print("exp", ref_perms(syms))
print("got", perms(syms))

syms = [0]
print("exp", ref_perms(syms))
print("got", perms(syms))

syms = [0, 1]
print("exp", ref_perms(syms))
print("got", perms(syms))


def fix(ps):
    return flatten([(flatten([xs[0], ys])) for ys in xs[1:]] for xs in ps[0])


syms = [0, 1, 2]
print("exp", ref_perms(syms))
print("got", fix(perms(syms)))

ps = perms(syms)
syms = [0, 1, 2, 4]
print("exp", ref_perms(syms))
print("got", fix(perms(syms)))


syms = ""
print("exp", ref_perms(syms))
print("got", perms(syms))

syms = "0"
print("exp", ref_perms(syms))
print("got", perms(syms))

syms = "01"
print("exp", ref_perms(syms))
print("got", perms(syms))

syms = "012"
print("exp", ref_perms(syms))
print("got", count_perms(syms))

ps = perms(syms)
syms = "0123"
print("exp", ref_perms(syms))
print("got", count_perms(syms))
