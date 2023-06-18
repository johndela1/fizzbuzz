def rand(n, bits=32):
    x = 123456789
    a = 5
    c = 33
    m = 2**bits

    while True:
        if n < 1:
            break
        n -= 1

        x = (a * x + c) & (m - 1)
        yield x

for n in rand(20, bits=5):
    print(n)
