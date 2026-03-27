def osszeg(n):
    if n == 0:
        return 0
    else:
        return n + osszeg(n - 1)