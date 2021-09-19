#!/usr/bin/env python3


def fizz_buzz_tr_2(n):
    out = ""
    if n % 3 == 0:
        out += "fizz"
    if n % 5 == 0:
        out += "buzz"
    if out == "":
        out = str(n)
    return out


def fizz_buzz_tr(n):
    fizz = "fizz" if n % 3 == 0 else ""
    buzz = "buzz" if n % 5 == 0 else ""
    return f"{fizz}{buzz}" or str(n)


def fizz_buzz():
    return ' '.join(fizz_buzz_tr(n) for n in range(1, 101))

if __name__ == "__main__":
    print(fizz_buzz())
