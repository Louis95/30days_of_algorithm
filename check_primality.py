def primeNative(n):
    if n < 2:
        return False
    for x in range(2, n):
        if (n % x) == 0:
            return False
    return True


print(primeNative(15)) 