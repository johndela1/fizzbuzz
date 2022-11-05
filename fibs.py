def fibs1(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
    return x

def fibs2(n, x=0, y=1):
    if n == 0: return x
    return fibs2(n-1, y, x+y)

def fibs3(n):
    if n < 2: return n
    return fibs3(n-1) + fibs3(n-2)

print([fibs1(i) for i in range(10)])
print([fibs2(i) for i in range(10)])
print([fibs3(i) for i in range(10)])
