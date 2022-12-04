def fib():
    prev, cur = 0, 1
    while True:
        yield cur
        prev, cur = cur, prev+cur