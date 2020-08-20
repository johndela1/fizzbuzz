#!/usr/bin/env python3


def fizz_buzz(n):
    out = ""
    if n % 3 == 0:
        out += "fizz"
    if n % 5 == 0:
        out += "buzz"
    if out == "":
        out = str(n)
    return out


def fizz_buzz_2(n):
    fizz = "" if n % 3 else "fizz"
    buzz = "" if n % 5 else "buzz"
    return f"{fizz}{buzz}" or str(n)


for f in (fizz_buzz, fizz_buzz_2):
    for n in range(1, 101):
        assert fizz_buzz(n) == fizz_buzz_2(n)
        print(f(n), end=" ")
    print()
