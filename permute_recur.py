# I know we don't handle len 0 or 1, this is just a POC

def _jjp(xs):
    def remove(x):
        xs2 = xs.copy()
        xs2.remove(x)
        return xs2

    if len(xs) == 2:
        return [[xs[0], xs[1]], [xs[1], xs[0]]]
    res = []
    for x in xs:
        for i in _jjp(remove(x)):
            res.append([x] + i)
    return res


def jjp(xs):
    return [tuple(i) for i in _jjp(xs)]


from itertools import permutations as pyp

assert jjp([0, 1, 2]) == [
    (0, 1, 2),
    (0, 2, 1),
    (1, 0, 2),
    (1, 2, 0),
    (2, 0, 1),
    (2, 1, 0),
]
xs = list(range(8))
assert jjp(xs), list(pyp(xs))
