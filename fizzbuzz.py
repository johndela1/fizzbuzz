#!/usr/bin/env python3


def fizz_buzz1(n):
    out = ""
    if n % 3 == 0:
        out += "fizz"
    if n % 5 == 0:
        out += "buzz"
    if out == "":
        out = str(n)
    return out


def fizz_buzz2(n):
    fizz = "" if n % 3 else "fizz"
    buzz = "" if n % 5 else "buzz"
    return f"{fizz}{buzz}" or str(n)


def fizz_buzz(f):
    return ' '.join(f(n) for n in range(1, 101))

if __name__ == "__main__":
    print(fizz_buzz(fizz_buzz2))
