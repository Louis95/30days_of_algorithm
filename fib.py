from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

def cum_sum(n):
    if n == 0:
        return 0
    return n + cum_sum(n-1)



