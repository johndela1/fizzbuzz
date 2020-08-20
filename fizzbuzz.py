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


for n in range(1, 101):
    print(fizz_buzz(n), end=" ")
print()
